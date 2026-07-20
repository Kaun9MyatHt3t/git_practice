from pydantic import BaseModel


class ChatCreate(BaseModel):
  question : str


class ChatUpdate(BaseModel):
  question : str
  answer : str


class ChatResponse(BaseModel):
  id : int
  question : str
  answer : str
  user_id : int

  class Config:
    from_attributes = True


class CreateUser(BaseModel):
  name : str
  email : str