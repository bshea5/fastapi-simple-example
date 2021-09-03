from typing import List, Optional
from pydantic import BaseModel
from sqlmodel import SQLModel

class UserCreate(SQLModel):
  name: str
  email: str
  password: str
class UserRead(SQLModel):
  id: int
  name: str
  email: str

  # Since we use this in a query, we need ORM model on.
  class Config():
    orm_mode = True

class Login(BaseModel):
  username: str
  password: str


class Token(BaseModel):
  access_token: str
  token_type: str


class TokenData(BaseModel):
  username: Optional[str] = None