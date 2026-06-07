from sqlalchemy import (
    Integer, String, DateTime, ForeignKey, Text
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)
from datetime import datetime
from typing import Optional

from app.db.database import Base


# app/models/trigger.py
from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
from typing import Optional


class Trigger(Base):
    __tablename__ = "triggers"

    id:       Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    habit_id: Mapped[int] = mapped_column(
        ForeignKey("habits.id"), nullable=False)  # ← changed
    context:  Mapped[Optional[str]] = mapped_column(Text)

    habit: Mapped["Habit"] = relationship(
        back_populates="triggers")  # ← changed

    def __repr__(self):
        return f"<Trigger id={self.id} context={self.context[:30]}>"
