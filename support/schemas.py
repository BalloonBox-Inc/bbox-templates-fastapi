from pydantic import BaseModel


# Admin
class AdminBase(BaseModel):
    email: str


class AdminCreate(AdminBase):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# User
class UserBase(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: str
    password: str
    is_active: bool
