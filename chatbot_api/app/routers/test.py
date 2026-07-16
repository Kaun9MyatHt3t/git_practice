from fastapi import APIRouter, Depends

router = APIRouter()


def check_user():
  return "User is valid"

@router.get("/test")
def test(value = Depends(check_user)):
  return {
    "message" : value
  }