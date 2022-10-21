
'''This module includes routers into the FastAPI framework.'''

from fastapi import APIRouter

from apis.routers import create_user, update_user


api_routers = APIRouter()
api_routers.include_router(create_user.router, prefix='/user', tags=['users'])
api_routers.include_router(update_user.router, prefix='/user', tags=['users'])
