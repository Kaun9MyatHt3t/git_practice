from fastapi import FastAPI, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel
from app.routers import chat, users, items, products, test
from dotenv import load_dotenv
from app.core.config import settings


load_dotenv()



app = FastAPI()

@app.get("/")
def home():
  return {"message" : settings.APP_NAME,
          "key" : settings.SECRET_KEY
          }


app.include_router(chat.router)

app.include_router(users.router)

app.include_router(items.router)

app.include_router(products.router)

app.include_router(test.router)






