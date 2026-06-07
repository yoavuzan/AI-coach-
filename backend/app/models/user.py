from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(200), unique=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        String(255), nullable=False)

    habits: Mapped[list["Habit"]] = relationship(
        back_populates="user",
        cascade="all, delete"
    )

    triggers: Mapped[list["Trigger"]] = relationship(
        back_populates="user",
        cascade="all, delete"
    )

    calendar_events: Mapped[list["CalendarEvent"]] = relationship(
        back_populates="user",
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"
