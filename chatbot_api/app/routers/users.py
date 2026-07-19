from fastapi import APIRouter, HTTPException, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User
from pydantic import BaseModel


router = APIRouter()


class CreateUser(BaseModel):
  name : str
  email : str


@router.post("/users", status_code = 201)
def create_user(user_input : CreateUser, db : Session = Depends(get_db)):
  existing_user = db.query(User).filter(User.email == user_input.email).first()

  if existing_user:
    raise HTTPException(
      status_code = 403,
      detail = "403: User already exists"
    )
  
  new_user = User(
    name = user_input.name,
    email = user_input.email
  )

  db.add(new_user)

  db.commit()

  return {
    "id": new_user.id,
    "name": new_user.name,
    "email": new_user.email
  }


@router.get("/users/{user_id}")
def get_user(user_id : int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first()

  if user is None:
    raise HTTPException(
      status_code=404,
      detail = "User not found"
    )
  return user


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
  users = db.query(User).all()

  return users


@router.put("/users/{user_id}")
def update_user(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first()

  if user is None:
    raise HTTPException(
      status_code = 404,
      detail = "404: User not found!"
    )

  user.email = "updated@gmail.com"

  db.commit()
  return {
    "id" : user.id,
    "email" : user.email,
    "name" : user.name
  }


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first()

  if user is None:
    raise HTTPException(
      status_code = 404,
      detail = "404: User not found!"
    )
  
  db.delete(user)
  db.commit()

  return {
    "message" : "User deleted"
  }


@router.get("/users/{user_id}/chats")
def get_user_chat(user_id: int, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == user_id).first()

  if user is None:
    raise HTTPException(
      status_code = 404,
      detail = "404: User not found!"
    )
  
  return user.chats

