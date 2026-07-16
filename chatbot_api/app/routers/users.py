from fastapi import APIRouter, HTTPException


router = APIRouter()



users = {
  1 : "K",
  2 : "J"
}

@router.get("/users/{user_id}")
def get_user(user_id : int):
  if user_id not in users:
    raise HTTPException(
      status_code=404,
      detail = "404 User not found"
    )
  return {
    "name" : users[user_id]
  }