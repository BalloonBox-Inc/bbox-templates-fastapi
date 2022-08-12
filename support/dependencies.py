from fastapi import Header, HTTPException, status
from dotenv import load_dotenv
from os import getenv
load_dotenv()


async def verify_admin_token(admin_token: str = Header()):
    if admin_token != getenv('ADMIN_TOKEN'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid admin token'
        )


async def verify_user_token(user_token: str = Header()):
    if user_token != getenv('USER_TOKEN'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid user token'
        )
