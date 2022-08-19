from pydantic import BaseModel


class AdminBase(BaseModel):
    email: str


class AdminCreate(AdminBase):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    username: str
    email: str
    password: str
