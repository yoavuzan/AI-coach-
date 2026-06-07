# app/crud/habit_log.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from datetime import datetime
from app.models.habit_log import HabitLog
from app.crud.habit import get_habit


# ── Create ────────────────────────────────────────────────────────────────────

def create_habit_log(
    db: Session,
    habit_id: int,
    user_id: int,
    status: str,
) -> HabitLog:
    # verify habit belongs to user before logging
    habit = get_habit(db, habit_id, user_id)
    if not habit:
        return None

    log = HabitLog(
        habit_id=habit_id,
        status=status,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


# ── Read ──────────────────────────────────────────────────────────────────────

def get_log(db: Session, log_id: int, user_id: int) -> Optional[HabitLog]:
    return db.execute(
        select(HabitLog)
        .join(HabitLog.habit)                   # join to habits table
        .where(HabitLog.id == log_id)
        .where(HabitLog.habit.has(user_id=user_id))  # ← ownership via habit
    ).scalar_one_or_none()


def get_logs_by_habit(
    db: Session,
    habit_id: int,
    user_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[HabitLog]:
    # verify habit belongs to user first
    habit = get_habit(db, habit_id, user_id)
    if not habit:
        return []

    return db.execute(
        select(HabitLog)
        .where(HabitLog.habit_id == habit_id)
        .offset(skip)
        .limit(limit)
        .order_by(HabitLog.timestamp.desc())
    ).scalars().all()


def get_logs_by_status(
    db: Session,
    habit_id: int,
    user_id: int,
    status: str,
) -> list[HabitLog]:
    habit = get_habit(db, habit_id, user_id)
    if not habit:
        return []

    return db.execute(
        select(HabitLog)
        .where(HabitLog.habit_id == habit_id)
        .where(HabitLog.status == status)
        .order_by(HabitLog.timestamp.desc())
    ).scalars().all()


def get_logs_by_date_range(
    db: Session,
    habit_id: int,
    user_id: int,
    start: datetime,
    end: datetime,
) -> list[HabitLog]:
    habit = get_habit(db, habit_id, user_id)
    if not habit:
        return []

    return db.execute(
        select(HabitLog)
        .where(HabitLog.habit_id == habit_id)
        .where(HabitLog.timestamp >= start)
        .where(HabitLog.timestamp <= end)
        .order_by(HabitLog.timestamp.desc())
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_log(
    db: Session,
    log_id: int,
    user_id: int,
    status: str,
) -> Optional[HabitLog]:
    log = get_log(db, log_id, user_id)  # ← ownership via habit
    if not log:
        return None

    log.status = status
    db.commit()
    db.refresh(log)
    return log


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_log(db: Session, log_id: int, user_id: int) -> bool:
    log = get_log(db, log_id, user_id)  # ← ownership via habit
    if not log:
        return False

    db.delete(log)
    db.commit()
    return True
