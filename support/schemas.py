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
