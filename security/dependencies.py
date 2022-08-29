from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from schemas.users import UserShow
from db import crud, models
from security import hashing
from config import settings


OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl='/admin/login')


def authenticate_user(db, email, password):

    user = crud.get_user_by_email(db, models.UserTable, email=email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid email')

    if not hashing.verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid password')

    return user


async def get_current_user(db, token: str = Depends(OAUTH2_SCHEME)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unable to authenticate token',
        headers={'WWW-Authenticate': 'Bearer'})

    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get('email')

        if email is None:
            raise credentials_exception

    except JWTError as e:
        raise credentials_exception from e

    user = crud.get_user_by_email(db, models.UserTable, email=email)

    if not user:
        raise credentials_exception

    return user


async def get_current_active_user(current_user: UserShow = Depends(get_current_user)):

    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Inactive user')

    return current_user
