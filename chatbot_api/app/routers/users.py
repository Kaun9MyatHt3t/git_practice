from fastapi import APIRouter, HTTPException, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app.models import User

router = APIRouter()


users = {
  1 : "K",
  2 : "J"
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
