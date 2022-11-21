'''This module defines the HTTP request schemas for the FastAPI routers.'''

from pydantic import BaseModel, EmailStr
from datetime import date


class UserCreate(BaseModel):
    '''Router schema to user/create'''

    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    '''Router schema to user/update'''

    email: EmailStr
    password: str
    is_active: bool


class User(BaseModel):
    '''User response model.'''

    email: str
    is_active: bool
    created_at: date
    updated_at: date
