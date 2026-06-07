from typing import Optional

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Habit(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    type: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    target_frequency: Mapped[Optional[int]] = mapped_column(Integer)

    user: Mapped["User"] = relationship(back_populates="habits")

    logs: Mapped[list["HabitLog"]] = relationship(
        back_populates="habit",
        cascade="all, delete"
    )

    conversations: Mapped[list["AIConversation"]] = relationship(
        back_populates="habit",
        cascade="all, delete"
    )

    # add to Habit model
    triggers: Mapped[list["Trigger"]] = relationship(
        back_populates="habit",
        cascade="all, delete"
    )
