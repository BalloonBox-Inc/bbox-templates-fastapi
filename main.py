from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from apis.routers import api_routers
from db import models, session, utils
from config import settings


def include_routers(app):
    app.include_router(api_routers)


def control_throttling(app):
    limiter = Limiter(key_func=get_remote_address, default_limits=['5/minute'])
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)


def create_database():
    models.Base.metadata.create_all(bind=session.engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_routers(app)
    control_throttling(app)
    create_database()
    return app


# initiate application
app = start_application()


# database securely managing session
@app.on_event('startup')
async def app_startup():
    await utils.check_db_connected()


@app.on_event('shutdown')
async def app_shutdown():
    await utils.check_db_disconnected()


# body request error handling
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'error': exc.errors()})
    )
