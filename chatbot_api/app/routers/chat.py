from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ChatHistory, User
from app.schemas import ChatCreate, ChatResponse, ChatUpdate


router = APIRouter()


def fetch_chat(db: Session, chat_id: int) -> ChatHistory:
  chat = db.query(ChatHistory).filter(ChatHistory.id == chat_id).first()
  if not chat:
    raise HTTPException(
     status_code = 404,
     detail = "404: Chat history not found"
    )
  return chat


@router.get("/chat/{chat_id}", response_model = ChatResponse)
def chat_history(chat_id : int, db : Session = Depends(get_db)):
  chat = fetch_chat(db, chat_id)
  
  return chat


@router.post("/chat", response_model = ChatResponse, status_code = 201)
def create_chat(request: ChatCreate, db: Session = Depends(get_db)):
  # user_check = db.query(User).filter(request.user_id == User.id).first()

  # if not user_check:
  #   raise HTTPException(
  #     status_code = 404,
  #     detail = "User not found"
  #   )

  chat_history = ChatHistory(
    question = request.question,
    answer = "test answer",
    user_id = 1
  )

  try:
    db.add(chat_history)
    db.commit()
    db.refresh(chat_history)

  except Exception:
    db.rollback()
    raise

  return chat_history


@router.put("/chat/{chat_id}")
def update_chat(request: ChatUpdate, chat_id: int, db: Session = Depends(get_db)):
  chat = fetch_chat(db, chat_id)
  
  chat.question = request.question
  chat.answer = request.answer

  try:
    db.commit()

  except Exception:
    db.rollback()
    raise

  return {
    "message" : "200 OK: Chat History Updated!"
  }


@router.delete("/chat/{chat_id}")
def delete_chat(chat_id: int, db: Session = Depends(get_db)):
  chat = fetch_chat(db, chat_id)
  
  try:
    db.delete(chat)
    db.commit()
    
  except Exception:
    db.rollback()
    raise

  return {
    "Status" : "204 No Content: Chat history deleted!"
  }

