from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/products/{product_id}")
def get_product( product_id : int, search : Optional[str]= None):
  return{
    "message" : f"You are looking for Product {product_id}",
    "search": search
  }
