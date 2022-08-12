from pydantic import BaseModel
from typing import Optional


# http request classes
class AdminBase(BaseModel):
    id: str
    email: str


class UserBase(BaseModel):
    id: str
    email: str
    password: str


# database classes
class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
