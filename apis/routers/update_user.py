'''This module manages the user update FastAPI router.'''

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from config import Settings
from apis import schemas
from database import crud
from database.session import get_db
from security import dependencies, get_settings


router = APIRouter()


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_user(
    item: schemas.UserUpdate,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings)
):  # pylint: disable=[W0613]
    '''
    Update a user data from database.

        :param email [str]: User email.
        :param password [str]: User password.
        :param is_active [bool]: User status.

        :returns [dict]: User has successfully been updated.

        :raises [HTTPException]:
            :[401] Unauthorized: 'Invalid email.' | 'Invalid password.
            :[409] Conflict: Unable to update object on database.
    '''

    # authenticate user
    user = dependencies.authenticate_user(
        db=db,
        item=item
    )

    # update user
    user.is_active = item.is_active
    crud.update_object(
        db=db,
        object=user
    )

    return dict(
        message='User has successfully been updated.'
    )
