from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ChatHistory


router = APIRouter()


class ChatRequest(BaseModel):
  question : str
  answer : str


class ChatResponse(BaseModel):
  your_question : str
  answer : str


def fetch_chat(db: Session, chat_id: int) -> ChatHistory:
  chat = db.query(ChatHistory).filter(ChatHistory.id == chat_id).first()
  if not chat:
    raise HTTPException(
     status_code = 404,
     detail = "404: Chat history not found"
    )
  return chat


@router.get("/chat/{chat_id}")
def chat_history(chat_id : int, db : Session = Depends(get_db)):
  chat = fetch_chat(db, chat_id)
  
  return {
    "question": chat.question,
    "answer": chat.answer,
    "time": chat.time
  }


@router.post("/chat", response_model = ChatResponse, status_code = 201)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
  chat_history = ChatHistory(
    question = request.question,
    answer = request.answer,
    user_id = 1
  )

  db.add(chat_history)
  db.commit()
  db.refresh(chat_history)

  return {
    "question" : request.question,
    "answer" : request.answer
  }


@router.put("/chat/{chat_id}")
def update_chat(request: ChatRequest, chat_id: int, db: Session = Depends(get_db)):
  chat = fetch_chat(db, chat_id)
  
  chat.question = request.question
  chat.answer = request.answer

  db.commit()

  return {
    "message" : "200 OK: Chat History Updated!"
  }


@router.delete("/chat/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
  chat = fetch_chat(db, chat_id)
  
  db.delete(chat)
  db.commit()

  return {
    "Status" : "204 No Content: Chat history deleted!"
  }

