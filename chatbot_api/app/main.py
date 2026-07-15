from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def home():
  return {"message" : "Chatbot api" }

@app.get("/users/{user_id}")
def get_user(user_id : int):
  return {
    "user_id" : user_id
  }


@app.get("/items")
def get_item(page : int, limit : int):
  return{
    "page" : page, 
    "limit" : limit
  }


@app.get("/products/{product_id}")
def get_product( product_id : int, search : Optional[str]= None):
  return{
    "message" : f"You are looking for Product {product_id}",
    "search": search
  }


@app.get("/chat")
def chat_history(page : int = 1, limit : int = 10):
  return {
    "page":page,
    "limit":limit,
    "messages":[
      "Hello", "How are you?"
    ]
  }