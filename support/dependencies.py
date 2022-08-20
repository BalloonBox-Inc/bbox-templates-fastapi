from fastapi import Depends, HTTPException, status
from support.oauth2 import get_current_user
from support import crud, hashing, schemas


def authenticate_user(db, email, password):
    user = crud.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid email')
    if not hashing.verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid password')
    return user


def get_current_active_user(current_user: schemas.UserBase = Depends(get_current_user)):
    if current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Inactive user')
    return current_user
