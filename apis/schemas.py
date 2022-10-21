'''This module defines the HTTP request schemas for the FastAPI routers.'''

from enum import Enum
from pydantic import BaseModel, EmailStr


class BlockchainNativeTokens(str, Enum):
    '''Define allowed blockchain native tokens.'''

    MATIC = 'MATIC'
    NEAR = 'NEAR'


class UserCreate(BaseModel):
    '''Router schema to user/create'''

    email: EmailStr
    password: str
    blockchain: BlockchainNativeTokens


class UserUpdate(BaseModel):
    '''Router schema to user/update'''

    email: EmailStr
    password: str
    is_active: bool
