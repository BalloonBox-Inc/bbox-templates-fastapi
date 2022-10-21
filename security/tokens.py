'''This module manages the creation of JWTs.'''

from datetime import datetime, timedelta
from jose import jwt

from config import settings


def create_jwt(data: dict):
    '''Create a JWT token.'''
    expire = datetime.utcnow() + timedelta(minutes=int(settings.SECURITY.JWT_EXPIRE_MINUTES))
    to_encode = data.copy()
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, settings.SECURITY.JWT_SECRET_KEY, algorithm=settings.SECURITY.JWT_ALGORITHM)


def decode_jwt(token: str):
    '''Decode a JWT token.'''
    return jwt.decode(token, settings.SECURITY.JWT_SECRET_KEY, algorithms=[settings.SECURITY.JWT_ALGORITHM])
