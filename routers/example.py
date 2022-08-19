from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from support.database import get_db
from support.dependencies import get_current_active_user
from support import crud, models, schemas


router = APIRouter(
    prefix='/example',
    tags=['Example'])


@router.post('/', status_code=status.HTTP_200_OK, summary='Example router')
async def example_router(request: Request, item: schemas.UserBase = Depends(get_current_active_user), db: Session = Depends(get_db)):
    '''
    Description

    Inputs:
    - **variable_name [dtype]**: description

    Outputs:
    - **variable_name [dtype]**: description
    '''

    print(f'\033[35;1m Request received from: {request.client.host}\033[0m')

    # get user by email
    user = crud.get_user_by_email(db, email=item.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already registered')

    # update user
    user.password = 'password'
    crud.update_row(db, obj=user)

    # add user
    crud.add_row(
        db, models.UserTable(
            email='email@example.com',
            hashed_password='encrypted_password',
            is_active=True))

    return {'error': False}
