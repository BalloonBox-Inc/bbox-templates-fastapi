'''This module manages the user creation FastAPI router.'''

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from apis.schemas import user
from database import crud, models
from database.session import get_db
from helpers.api_exceptions import ExceptionFormatter
from security.hashing import SecureHash


router = APIRouter()


@router.post('/create', status_code=status.HTTP_200_OK)
async def create_user(
    item: user.UserCreate,
    db: Session = Depends(get_db)
):
    '''
    Create a user and store to database.

        :param email [str]: User email.
        :param password [str]: User password.

        :returns [dict]: User has successfully been created.

        :raises [HTTPException]:
            :[400] Bad request: Email object already exists.
            :[409] Conflict: Unable to add object to database.
    '''

    # check if user exists
    user = crud.get_object(
        db=db,
        table=models.UserTable,
        column=models.UserTable.email,
        value=item.email
    )
    if user:
        raise ExceptionFormatter(
            status_code=status.HTTP_400_BAD_REQUEST,
            message='Email already exists.'
        )

    # add user
    crud.create_object(
        db=db,
        object=models.UserTable(
            email=item.email,
            hashed_password=SecureHash.create(item.password),
            is_active=True
        )
    )

    return dict(
        message='User has successfully been created.'
    )
