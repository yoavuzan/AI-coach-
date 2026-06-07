# app/crud/trigger.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from app.models.trigger import Trigger
from app.crud.habit import get_habit


# ── Create ────────────────────────────────────────────────────────────────────

def create_trigger(
    db: Session,
    habit_id: int,
    user_id: int,
    context: str,
) -> Optional[Trigger]:
    habit = get_habit(db, habit_id, user_id)  # ← verify ownership via habit
    if not habit:
        return None

    trigger = Trigger(habit_id=habit_id, context=context)
    db.add(trigger)
    db.commit()
    db.refresh(trigger)
    return trigger


# ── Read ──────────────────────────────────────────────────────────────────────

def get_trigger(db: Session, trigger_id: int, user_id: int) -> Optional[Trigger]:
    return db.execute(
        select(Trigger)
        .join(Trigger.habit)
        .where(Trigger.id == trigger_id)
        .where(Trigger.habit.has(user_id=user_id))  # ← ownership via habit
    ).scalar_one_or_none()


def get_triggers_by_habit(
    db: Session,
    habit_id: int,
    user_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[Trigger]:
    habit = get_habit(db, habit_id, user_id)  # ← verify ownership
    if not habit:
        return []

    return db.execute(
        select(Trigger)
        .where(Trigger.habit_id == habit_id)
        .offset(skip)
        .limit(limit)
    ).scalars().all()


def search_triggers(
    db: Session,
    habit_id: int,
    user_id: int,
    keyword: str,
) -> list[Trigger]:
    habit = get_habit(db, habit_id, user_id)  # ← verify ownership
    if not habit:
        return []

    return db.execute(
        select(Trigger)
        .where(Trigger.habit_id == habit_id)
        .where(Trigger.context.ilike(f"%{keyword}%"))
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_trigger(
    db: Session,
    trigger_id: int,
    user_id: int,
    context: str,
) -> Optional[Trigger]:
    trigger = get_trigger(db, trigger_id, user_id)  # ← ownership via habit
    if not trigger:
        return None

    trigger.context = context
    db.commit()
    db.refresh(trigger)
    return trigger


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_trigger(db: Session, trigger_id: int, user_id: int) -> bool:
    trigger = get_trigger(db, trigger_id, user_id)  # ← ownership via habit
    if not trigger:
        return False

    db.delete(trigger)
    db.commit()
    return True
