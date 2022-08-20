from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from support.database import get_db
from support import crud, dependencies, hashing, models, schemas


router = APIRouter(
    prefix='/user',
    tags=['User'])


@router.post('/create', status_code=status.HTTP_200_OK)
async def create_user(request: Request, item: schemas.UserBase, db: Session = Depends(get_db)):
    '''
    Description

    Inputs:
    - **email [str]**: user email
    - **password [str]**: user password

    Outputs:
    - **[object]**: {
        'error': False,
        'detail': 'User has successfully been created'
        }
    '''

    print(f'\033[35;1m Request received from: {request.client.host}\033[0m')

    # check if user exists
    user = crud.get_user_by_email(db, email=item.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already registered')

    # add user
    crud.add_row(
        db, models.UserTable(
            email=item.email,
            hashed_password=hashing.encrypt_password(item.password),
            is_active=True))

    return {'error': False, 'detail': 'User has successfully been created'}


@router.post('/update', status_code=status.HTTP_200_OK)
async def update_user(request: Request, item: schemas.UserUpdate, db: Session = Depends(get_db)):
    '''
    Description

    Inputs:
    - **email [str]**: user email
    - **password [str]**: user password
    - **is_active [bool]**: user status

    Outputs:
    - **[object]**: {
        'error': False,
        'detail': 'User has successfully been updated'
        }
    '''

    print(f'\033[35;1m Request received from: {request.client.host}\033[0m')

    # authenticate user
    user = dependencies.authenticate_user(db, email=item.email, password=item.password)

    # update user
    user.is_active = item.is_active
    crud.update_row(db, obj=user)

    return {'error': False, 'detail': 'User has successfully been updated'}
