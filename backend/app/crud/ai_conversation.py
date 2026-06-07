# app/crud/ai_conversation.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from app.models.ai_conversation import AIConversation
from app.crud.habit import get_habit


# ── Create ────────────────────────────────────────────────────────────────────

def create_conversation(
    db: Session,
    habit_id: int,
    user_id: int,
    title: Optional[str] = None,
) -> Optional[AIConversation]:
    habit = get_habit(db, habit_id, user_id)  # ← verify ownership
    if not habit:
        return None

    conversation = AIConversation(habit_id=habit_id, title=title)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


# ── Read ──────────────────────────────────────────────────────────────────────

def get_conversation(
    db: Session,
    conversation_id: int,
    user_id: int,
) -> Optional[AIConversation]:
    return db.execute(
        select(AIConversation)
        .join(AIConversation.habit)
        .where(AIConversation.id == conversation_id)
        # ← ownership via habit
        .where(AIConversation.habit.has(user_id=user_id))
    ).scalar_one_or_none()


def get_conversations_by_habit(
    db: Session,
    habit_id: int,
    user_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[AIConversation]:
    habit = get_habit(db, habit_id, user_id)  # ← verify ownership
    if not habit:
        return []

    return db.execute(
        select(AIConversation)
        .where(AIConversation.habit_id == habit_id)
        .order_by(AIConversation.created_at.desc())
        .offset(skip)
        .limit(limit)
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_conversation(
    db: Session,
    conversation_id: int,
    user_id: int,
    title: Optional[str] = None,
) -> Optional[AIConversation]:
    conversation = get_conversation(
        db, conversation_id, user_id)  # ← ownership via habit
    if not conversation:
        return None

    if title is not None:
        conversation.title = title

    db.commit()
    db.refresh(conversation)
    return conversation


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_conversation(
    db: Session,
    conversation_id: int,
    user_id: int,
) -> bool:
    conversation = get_conversation(
        db, conversation_id, user_id)  # ← ownership via habit
    if not conversation:
        return False

    db.delete(conversation)
    db.commit()
    return True
