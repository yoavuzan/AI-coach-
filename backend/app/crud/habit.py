# app/crud/habit.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from app.models.habit import Habit


# ── Create ────────────────────────────────────────────────────────────────────

def create_habit(
    db: Session,
    user_id: int,
    name: str,
    type: str,
    target_frequency: Optional[int] = None,
) -> Habit:
    habit = Habit(
        user_id=user_id,
        name=name,
        type=type,
        target_frequency=target_frequency,
    )
    db.add(habit)
    db.commit()
    db.refresh(habit)
    return habit


# ── Read ──────────────────────────────────────────────────────────────────────

def get_habit(db: Session, habit_id: int, user_id: int) -> Optional[Habit]:
    return db.execute(
        select(Habit)
        .where(Habit.id == habit_id)
        .where(Habit.user_id == user_id)  # ← always both
    ).scalar_one_or_none()


def get_habits_by_user(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[Habit]:
    return db.execute(
        select(Habit)
        .where(Habit.user_id == user_id)
        .offset(skip)
        .limit(limit)
    ).scalars().all()


def get_habits_by_type(
    db: Session,
    user_id: int,
    type: str,
) -> list[Habit]:
    return db.execute(
        select(Habit)
        .where(Habit.user_id == user_id)  # ← always both
        .where(Habit.type == type)
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_habit(
    db: Session,
    habit_id: int,
    user_id: int,
    name: Optional[str] = None,
    type: Optional[str] = None,
    target_frequency: Optional[int] = None,
) -> Optional[Habit]:
    habit = get_habit(db, habit_id, user_id)  # ← always both
    if not habit:
        return None

    if name is not None:
        habit.name = name
    if type is not None:
        habit.type = type
    if target_frequency is not None:
        habit.target_frequency = target_frequency

    db.commit()
    db.refresh(habit)
    return habit


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_habit(db: Session, habit_id: int, user_id: int) -> bool:
    habit = get_habit(db, habit_id, user_id)  # ← always both
    if not habit:
        return False

    db.delete(habit)
    db.commit()
    return True
