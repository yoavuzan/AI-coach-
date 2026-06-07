from sqlalchemy import (
    Integer, String, DateTime, ForeignKey
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)
from datetime import datetime
from typing import Optional

from app.db.database import Base


class AIConversation(Base):
    __tablename__ = "ai_conversations"

    id:         Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    habit_id:   Mapped[int] = mapped_column(
        ForeignKey("habits.id"), nullable=True)
    title:      Mapped[Optional[str]] = mapped_column(String(300))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime, onupdate=datetime.utcnow)

    habit:    Mapped["Habit"] = relationship(back_populates="conversations")
    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation", cascade="all, delete")

    def __repr__(self):
        return f"<AIConversation id={self.id} habit_id={self.habit_id}>"
