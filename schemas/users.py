from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserShow(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    is_active: bool
