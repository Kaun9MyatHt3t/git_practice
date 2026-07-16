from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
  question : str


class ChatResponse(BaseModel):
  your_question : str
  answer : str


@router.get("/chat")
def chat_history(page : int = 1, limit : int = 10):
  return {
    "page":page,
    "limit":limit,
    "messages":[
      "Hello", "How are you?"
    ]
  }

@router.post("/chat", response_model = ChatResponse)
def chat(request : ChatRequest):
  return{
    "your_question" : request.question,
    "answer" : f"you asked : {request.question}"
  }