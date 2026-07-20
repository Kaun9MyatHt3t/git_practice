from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


DATABASE_URL = "postgresql+psycopg://postgres:root@localhost:5432/orm_learning"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
  pass

def get_db()->Generator[Session, None, None]:
  db = SessionLocal()

  try:
    yield db

  finally:
    db.close()