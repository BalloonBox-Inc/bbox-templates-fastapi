'''This module initiates the FastAPI application and the Database session.'''

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from apis.middleware import api_routers
from apis.exceptions import ExceptionFormatter
from database import models, session, utils
from config import settings


def include_routers(app):
    '''Add routers to the FastAPI framework.'''
    app.include_router(api_routers)


def control_throttling(app):
    '''Limit the amount of requests per minute based on IP address.'''
    limiter = Limiter(key_func=get_remote_address, default_limits=['5/minute'])
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)


def create_database():
    '''Initiate the database session.'''
    models.Base.metadata.create_all(bind=session.engine)


def start_application():
    '''Initiate the FastAPI application.'''
    app = FastAPI(title=settings.APP.PROJECT_NAME, version=settings.APP.PROJECT_VERSION)
    include_routers(app)
    control_throttling(app)
    create_database()
    return app


# initiate application
app = start_application()


# database securely managing session
@app.on_event('startup')
async def app_startup():
    '''Ensure that the connection with the database has been established.'''
    await utils.check_db_connected()


@app.on_event('shutdown')
async def app_shutdown():
    '''Ensure that the connection with the database has been terminated.'''
    await utils.check_db_disconnected()


# body request error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):  # pylint: disable=[W0613]
    '''Ensure that the parameters passed by the HTTP request follow the defined schemas.'''
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            dict(
                error=True,
                message=exc.errors()
            )
        )
    )


# custom exception handler
@app.exception_handler(ExceptionFormatter)
async def standard_exception_handler(request: Request, exc: ExceptionFormatter):  # pylint: disable=[W0613]
    '''Ensure errors are standardized.'''
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            dict(
                error=True,
                message=exc.message
            )
        )
    )
