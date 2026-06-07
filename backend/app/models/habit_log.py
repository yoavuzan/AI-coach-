from sqlalchemy import Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.db.database import Base


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id:        Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    habit_id:  Mapped[int] = mapped_column(
        ForeignKey("habits.id"), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    status:    Mapped[str] = mapped_column(
        Enum("done", "failed", name="log_status"), nullable=False)

    habit: Mapped["Habit"] = relationship(back_populates="logs")

    def __repr__(self):
        return f"<HabitLog id={self.id} status={self.status} at={self.timestamp}>"
