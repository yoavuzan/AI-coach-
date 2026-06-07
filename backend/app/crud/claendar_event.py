# app/crud/calendar_event.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from datetime import datetime
from app.models.calendar_event import CalendarEvent


# ── Create ────────────────────────────────────────────────────────────────────

def create_calendar_event(
    db: Session,
    user_id: int,
    title: str,
    start_time: datetime,
    end_time: Optional[datetime] = None,
) -> CalendarEvent:
    event = CalendarEvent(
        user_id=user_id,
        title=title,
        start_time=start_time,
        end_time=end_time,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


# ── Read ──────────────────────────────────────────────────────────────────────

def get_event(db: Session, event_id: int, user_id: int) -> Optional[CalendarEvent]:
    return db.execute(
        select(CalendarEvent)
        .where(CalendarEvent.id == event_id)
        .where(CalendarEvent.user_id == user_id)  # ← always both
    ).scalar_one_or_none()


def get_events_by_user(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[CalendarEvent]:
    return db.execute(
        select(CalendarEvent)
        .where(CalendarEvent.user_id == user_id)
        .order_by(CalendarEvent.start_time.asc())
        .offset(skip)
        .limit(limit)
    ).scalars().all()


def get_events_by_date_range(
    db: Session,
    user_id: int,
    start: datetime,
    end: datetime,
) -> list[CalendarEvent]:
    return db.execute(
        select(CalendarEvent)
        .where(CalendarEvent.user_id == user_id)
        .where(CalendarEvent.start_time >= start)
        .where(CalendarEvent.start_time <= end)
        .order_by(CalendarEvent.start_time.asc())
    ).scalars().all()


def get_upcoming_events(
    db: Session,
    user_id: int,
    limit: int = 10,
) -> list[CalendarEvent]:
    return db.execute(
        select(CalendarEvent)
        .where(CalendarEvent.user_id == user_id)
        .where(CalendarEvent.start_time >= datetime.utcnow())
        .order_by(CalendarEvent.start_time.asc())
        .limit(limit)
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_event(
    db: Session,
    event_id: int,
    user_id: int,
    title: Optional[str] = None,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
) -> Optional[CalendarEvent]:
    event = get_event(db, event_id, user_id)  # ← always both
    if not event:
        return None

    if title is not None:
        event.title = title
    if start_time is not None:
        event.start_time = start_time
    if end_time is not None:
        event.end_time = end_time

    db.commit()
    db.refresh(event)
    return event


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_event(db: Session, event_id: int, user_id: int) -> bool:
    event = get_event(db, event_id, user_id)  # ← always both
    if not event:
        return False

    db.delete(event)
    db.commit()
    return True
