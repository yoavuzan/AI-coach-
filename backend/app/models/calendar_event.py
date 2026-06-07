from sqlalchemy import (
    Integer, String, DateTime, ForeignKey
)
from sqlalchemy.orm import (
    Mapped, mapped_column, relationship
)
from datetime import datetime
from typing import Optional

from app.db.database import Base


class CalendarEvent(Base):
    __tablename__ = "calendar_events"

    id:         Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    user_id:    Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    title:      Mapped[str] = mapped_column(String(300), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time:   Mapped[Optional[datetime]] = mapped_column(DateTime)

    user: Mapped["User"] = relationship(back_populates="calendar_events")

    def __repr__(self):
        return f"<CalendarEvent id={self.id} title={self.title}>"
