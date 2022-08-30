from fastapi import APIRouter
from apis import user


api_routers = APIRouter()
api_routers.include_router(user.router, prefix='/user', tags=['users'])
