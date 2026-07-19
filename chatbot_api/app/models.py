from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import engine, Base
from datetime import datetime, UTC


class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)

  chats = relationship("ChatHistory")


class ChatHistory(Base):
  __tablename__ = "chat_history"

  id = Column(Integer, primary_key=True)
  question = Column(String)
  answer = Column(String)
  time = Column(DateTime, default=datetime.now(UTC))

  user_id = Column(Integer, ForeignKey("users.id"))
  user = relationship("User")
