from sqlalchemy import (
    Integer, DateTime, ForeignKey, Enum, Text
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)
from datetime import datetime

from app.db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id:              Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("ai_conversations.id"), nullable=False)
    role:            Mapped[str] = mapped_column(
        Enum("user", "assistant", name="message_role"), nullable=False)
    content:         Mapped[str] = mapped_column(Text, nullable=False)
    created_at:      Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)

    conversation: Mapped["AIConversation"] = relationship(
        back_populates="messages")

    def __repr__(self):
        return f"<Message id={self.id} role={self.role}>"
