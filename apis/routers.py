from fastapi import APIRouter
from apis import example


api_routers = APIRouter()
api_routers.include_router(example.router, prefix='/example', tags=['example'])
