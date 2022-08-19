from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from helpers.support_files import read_env_vars
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional


JWT_SECRET_KEY = read_env_vars('JWT_SECRET_KEY')
JWT_ALGORITHM = read_env_vars('JWT_ALGORITHM')
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl='/admin/login')


def create_access_token(data: dict, expires_delta: Optional[int] = None):

    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode = data.copy()
    to_encode.update({'exp': expire})

    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


async def get_current_user(token: str = Depends(OAUTH2_SCHEME)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unable to authenticate token',
        headers={'WWW-Authenticate': 'Bearer'})

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email: str = payload.get('email')
        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    return payload
