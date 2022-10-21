'''This module manages global application dependencies.'''

from functools import lru_cache
from fastapi import status
from sqlalchemy.orm import Session

from config import settings
from apis import schemas
from apis.exceptions import ExceptionFormatter, exc
from database import crud, models
from security import hashing


@lru_cache()
def get_settings():
    '''Use the @lru_cache() decorator to create Settings object only once, instead of doing it for each request.
    Learn more at https://fastapi.tiangolo.com/it/advanced/settings/#creating-the-settings-only-once-with-lru_cache'''
    return settings


def authenticate_user(db: Session, item: schemas.UserUpdate):
    '''Ensure user is authenticated.'''

    user = crud.get_object(
        db=db,
        table=models.UserTable,
        column=models.UserTable.email,
        value=item.email
    )
    if not user:
        raise ExceptionFormatter(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message=exc.NOT_EMAIL
        )

    if not hashing.verify_hash(item.password, user.hashed_password):
        raise ExceptionFormatter(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message=exc.NOT_PASSWORD
        )

    return user
