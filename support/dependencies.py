from fastapi import Header, HTTPException, status
from helpers.support_files import read_env_vars


async def verify_admin_token(admin_token: str = Header()):
    if admin_token != read_env_vars('ADMIN_TOKEN'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid admin token'
        )


async def verify_user_token(user_token: str = Header()):
    if user_token != 'fake-super-secret-token':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid user token'
        )
