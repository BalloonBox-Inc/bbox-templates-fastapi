'''This module manages the user creation FastAPI router.'''

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from config import Settings
from apis import schemas
from apis.exceptions import ExceptionFormatter, exc
from database import crud, models
from database.session import get_db
from security import hashing, get_settings


router = APIRouter()


@router.post('/create', status_code=status.HTTP_200_OK)
async def create_user(
    item: schemas.UserCreate,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings)
):  # pylint: disable=[W0613]
    '''
    Create a user and store to database.

        :param email [str]: User email.
        :param password [str]: User password.
        :param blockchain [str]: The blockchain on which to create the user.

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
            message=exc.DB_EXISTING_OBJECT.format('Email')
        )

    # add user
    crud.create_object(
        db=db,
        object=models.UserTable(
            email=item.email,
            hashed_password=hashing.generate_hash(item.password),
            blockchain=item.blockchain,
            is_active=True
        )
    )

    return dict(
        message='User has successfully been created.'
    )
