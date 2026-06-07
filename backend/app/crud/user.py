
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from typing import Optional


# ── Create ────────────────────────────────────────────────────────────────────

def create_user(db: Session, name: str, email: str, password: str) -> User:
    # check if email already exists
    existing = db.execute(select(User).where(
        User.email == email)).scalar_one_or_none()
    if existing:
        raise ValueError(f"Email '{email}' is already registered")

    user = User(name=name, email=email)
    user.set_password(password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# ── Read ──────────────────────────────────────────────────────────────────────

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.get(User, user_id)


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.execute(
        select(User).where(User.email == email)
    ).scalar_one_or_none()


def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.execute(
        select(User).offset(skip).limit(limit)
    ).scalars().all()


# ── Update ────────────────────────────────────────────────────────────────────

def update_user(
    db: Session,
    user_id: int,
    name: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
) -> Optional[User]:
    user = db.get(User, user_id)
    if not user:
        return None

    if name:
        user.name = name
    if email:
        user.email = email
    if password:
        user.set_password(password)

    db.commit()
    db.refresh(user)
    return user


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_user(db: Session, user_id: int) -> bool:
    user = db.get(User, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
