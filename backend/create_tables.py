from app.db.base import Base
from app.db.database import engine

# Import all ORM models
from app.models import models

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")