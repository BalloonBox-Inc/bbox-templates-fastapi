'''This module manages the user update FastAPI router.'''

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from apis.schemas import user
from database import crud, models
from database.session import get_db
from security.dependencies import authenticate_user


router = APIRouter()


@router.post('/update', status_code=status.HTTP_200_OK, dependencies=[Depends(authenticate_user)], response_model=user.User)
async def update_user(
    item: user.UserUpdate,
    db: Session = Depends(get_db)
):
    '''
    Update a user data profile.

        :param email [str]: User email.
        :param password [str]: User password.
        :param is_active [bool]: User status.

        :returns [dict]: User has successfully been updated.
    '''

    crud.update_object(
        db=db,
        table=models.UserTable,
        column=models.UserTable.email,
        value=item.email,
        object=dict(is_active=item.is_active)
    )

    return dict(
        message='User has successfully been updated.'
    )
