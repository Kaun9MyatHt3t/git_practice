from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"message" : "Chatbot api" }

@app.get("/users/{user_id}")
def get_user(user_id : int):
  return {
    "user_id" : user_id
  }

@app.get("/products/{product_id}")
def get_product(product_id : int):
  return {
    "message" : f"You are looking for Product {product_id}" 
  }