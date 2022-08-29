from pydantic import BaseModel, EmailStr


class AdminCreate(BaseModel):
    email: EmailStr
    password: str


class AdminShow(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class AdminUpdate(BaseModel):
    email: EmailStr
    password: str
    is_active: bool
