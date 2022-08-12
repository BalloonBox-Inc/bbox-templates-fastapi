from fastapi import APIRouter, Depends, Request, Response, HTTPException, status
from sqlalchemy.orm import Session
from support.database import get_db
from support.dependencies import verify_user_token
from support.schemas import UserBase
from support import crud


router = APIRouter(
    prefix='/example',
    tags=['Example'],
    dependencies=[Depends(verify_user_token)]
)


@router.post('/', status_code=status.HTTP_200_OK, summary='Example router')
async def example_router(request: Request, response: Response, item: UserBase, db: Session = Depends(get_db)):
    '''
    Description

    Inputs:
    - **variable_name [dtype]**: description

    Outputs:
    - **variable_name [dtype]**: description
    '''

    print(f'\033[35;1m Request received from: {request.client.host}\033[0m')

    user = crud.get_user_by_email(db, email=item.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email already registered'
        )

    return crud.create_user(db=db, user=item.email)
