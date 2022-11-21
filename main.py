'''This module initiates the FastAPI application and the Database session.'''

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from config import get_settings
from apis.middleware import api_routers
from database import models, session
from database.startup import setup_database
from helpers.api_exceptions import ExceptionFormatter
from helpers.api_routers import APIRouters
from helpers.app_throttling import Throttling


def create_database():
    '''Initiate the database session.'''
    models.Base.metadata.create_all(bind=session.engine)
    setup_database()


def start_application():
    '''Initiate the FastAPI application.'''
    settings = get_settings()
    app = FastAPI(title=settings.APP.PROJECT_NAME, version=settings.APP.PROJECT_VERSION)
    app = Throttling.enable(app)
    app = APIRouters.include(app, api_routers)

    create_database()
    return app


# initiate application
app = start_application()


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
