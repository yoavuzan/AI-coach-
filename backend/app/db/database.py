from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite:///habit_tracker.db"


class Base(DeclarativeBase):
    pass


engine = create_engine(DATABASE_URL, echo=True)
