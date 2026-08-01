from dotenv import load_dotenv
load_dotenv()

import os
from sqlalchemy import create_engine

print("DATABASE_URL =", os.getenv("DATABASE_URL"))

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.connect() as conn:
    print("Connected successfully!")