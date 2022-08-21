from fastapi import APIRouter, Depends, Request, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from helpers.support_files import read_env_vars
from support import dependencies, schemas
from support.oauth2 import create_access_token


router = APIRouter(
    prefix='/admin',
    tags=['Admin'])


@router.post('/', status_code=status.HTTP_200_OK, summary='Example admin')
async def example_admin(request: Request, item: schemas.AdminBase, form_data: OAuth2PasswordRequestForm = Depends()):
    '''
    Description

    Inputs:
    - **variable_name [dtype]**: description

    Outputs:
    - **variable_name [dtype]**: description
    '''

    print(f'\033[35;1m Request received from: {request.client.host}\033[0m')

    user = dependencies.authenticate_user(item.__dict__, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Bearer'})

    access_token = create_access_token(
        data={'sub': user.username}, expires_delta=read_env_vars('ACCESS_TOKEN_EXPIRE_MINUTES'))

    return {'access_token': access_token, 'token_type': 'bearer'}
