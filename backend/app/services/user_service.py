from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User
from app.crud.user import (
    get_user_by_id,
    get_user_by_email,
    get_all_users,
)

pwd_context = CryptContext(
    schemes=["bcrypt"], deprecated="auto")


# ── Register ──────────────────────────────────────────────────────────────────

def register_user(db: Session, name: str, email: str, password: str) -> User:
    if not name or not email or not password:
        raise ValueError("Name, email and password are required")

    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    existing = get_user_by_email(db, email)
    if existing:
        raise ValueError("Email already registered")

    password_hash = pwd_context.hash(password)

    user = User(name=name, email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# ── Login ─────────────────────────────────────────────────────────────────────

def login_user(db: Session, email: str, password: str) -> User:
    if not email or not password:
        raise ValueError("Email and password are required")

    user = get_user_by_email(db, email)

    # same message for wrong email or wrong password (security best practice)
    if not user or not pwd_context.verify(password, user.password_hash):
        raise ValueError("Invalid email or password")

    return user


# ── Get user ──────────────────────────────────────────────────────────────────

def get_user(db: Session, user_id: int) -> User:
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    if limit > 100:
        raise ValueError("Limit cannot exceed 100")
    return get_all_users(db, skip=skip, limit=limit)


# ── Update ────────────────────────────────────────────────────────────────────

def update_user(
    db: Session,
    user_id: int,
    name: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
) -> User:
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")

    if name:
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
        user.name = name

    if email:
        existing = get_user_by_email(db, email)
        if existing and existing.id != user_id:
            raise ValueError("Email already taken by another user")
        user.email = email

    if password:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        user.password_hash = pwd_context.hash(password)

    db.commit()
    db.refresh(user)
    return user


# ── Change password ───────────────────────────────────────────────────────────

def change_password(
    db: Session,
    user_id: int,
    old_password: str,
    new_password: str,
) -> User:
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")

    if not pwd_context.verify(old_password, user.password_hash):
        raise ValueError("Current password is incorrect")

    if len(new_password) < 8:
        raise ValueError("New password must be at least 8 characters")

    if old_password == new_password:
        raise ValueError(
            "New password must be different from current password")

    user.password_hash = pwd_context.hash(new_password)
    db.commit()
    db.refresh(user)
    return user


# ── Delete ────────────────────────────────────────────────────────────────────

def delete_user(db: Session, user_id: int, password: str) -> bool:
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError(f"User {user_id} not found")

    # require password confirmation before deleting
    if not pwd_context.verify(password, user.password_hash):
        raise ValueError("Password incorrect")

    db.delete(user)
    db.commit()
    return True
