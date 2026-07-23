from app.db.base import Base
from app.db.database import engine

# Import all models here so SQLAlchemy knows about them
from app.models.prompt import Prompt


def init_db():
    Base.metadata.create_all(bind=engine)