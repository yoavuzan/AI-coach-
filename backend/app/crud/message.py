# app/crud/message.py
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from app.models.message import Message
from app.crud.ai_conversation import get_conversation


# ── Create ────────────────────────────────────────────────────────────────────

def create_message(
    db: Session,
    conversation_id: int,
    user_id: int,
    role: str,
    content: str,
) -> Optional[Message]:
    # verify conversation belongs to user via habit chain
    conversation = get_conversation(db, conversation_id, user_id)
    if not conversation:
        return None

    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


# ── Read ──────────────────────────────────────────────────────────────────────

def get_message(
    db: Session,
    message_id: int,
    user_id: int,
) -> Optional[Message]:
    return db.execute(
        select(Message)
        .join(Message.conversation)
        .join(Message.conversation.property.mapper.class_.habit)
        .where(Message.id == message_id)
        .where(Message.conversation.has(
            AIConversation.habit.has(user_id=user_id)  # ← ownership via chain
        ))
    ).scalar_one_or_none()


def get_messages_by_conversation(
    db: Session,
    conversation_id: int,
    user_id: int,
    skip: int = 0,
    limit: int = 100,
) -> list[Message]:
    # verify conversation belongs to user first
    conversation = get_conversation(db, conversation_id, user_id)
    if not conversation:
        return []

    return db.execute(
        select(Message)
        .where(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.asc())  # asc — chronological order
        .offset(skip)
        .limit(limit)
    ).scalars().all()


def get_messages_by_role(
    db: Session,
    conversation_id: int,
    user_id: int,
    role: str,
) -> list[Message]:
    conversation = get_conversation(db, conversation_id, user_id)
    if not conversation:
        return []

    return db.execute(
        select(Message)
        .where(Message.conversation_id == conversation_id)
        .where(Message.role == role)
        .order_by(Message.created_at.asc())
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_message(
    db: Session,
    message_id: int,
    user_id: int,
    content: str,
) -> Optional[Message]:
    message = get_message(db, message_id, user_id)  # ← ownership via chain
    if not message:
        return None

    message.content = content
    db.commit()
    db.refresh(message)
    return message


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_message(
    db: Session,
    message_id: int,
    user_id: int,
) -> bool:
    message = get_message(db, message_id, user_id)  # ← ownership via chain
    if not message:
        return False

    db.delete(message)
    db.commit()
    return True
