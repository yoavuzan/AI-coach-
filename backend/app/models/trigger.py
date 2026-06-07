from sqlalchemy import (
    Integer, String, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)
from datetime import datetime
from typing import Optional

from app.db.database import Base


class Trigger(Base):
    __tablename__ = "triggers"

    id:      Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    context: Mapped[Optional[str]] = mapped_column(
        Text)  # time, event, behavior pattern

    user: Mapped["User"] = relationship(back_populates="triggers")

    def __repr__(self):
        return f"<Trigger id={self.id} context={self.context[:30]}>"
