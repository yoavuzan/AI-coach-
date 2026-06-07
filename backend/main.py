from app.db.database import Base, engine

# Import all models so they register with Base.metadata
from app.models import *

Base.metadata.create_all(engine)
