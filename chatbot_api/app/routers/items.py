from fastapi import APIRouter

router = APIRouter()

@router.get("/items")
def get_item(page : int, limit : int):
  return{
    "page" : page, 
    "limit" : limit
  }
