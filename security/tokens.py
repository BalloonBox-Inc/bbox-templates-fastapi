from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from config import settings


def create_access_token(data: dict, expires_delta: Optional[int] = None):

    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode = data.copy()
    to_encode.update({'exp': expire})

    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
