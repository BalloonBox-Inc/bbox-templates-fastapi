'''This module manages FastAPI exceptions.'''

from fastapi import HTTPException


class ExceptionFormatter(Exception):
    '''Create a custom exception.'''

    def __init__(self, status_code: HTTPException, message: str):
        self.status_code = status_code
        self.message = message


class ExceptionMessage():
    '''API error messages.'''

    # Printing Logs
    RED = '\033[0;31m ERROR'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m WARNING'
    CLOSE_ASCII = '\033[0m'

    # Database
    DB_CONNECT = 'Unable to connect with database.'
    DB_DISCONNECT = 'Unable to disconnect from database.'
    DB_CREATE_OBJECT = 'Unable to add object to database.'
    DB_UPDATE_OBJECT = 'Unable to update object on database.'
    DB_DELETE_OBJECT = 'Unable to delete object from database.'
    DB_EXISTING_OBJECT = 'Database object already exists.'

    # Notifications
    EMAIL_NOTIFICATION = 'Unable to send email notification.'


error = ExceptionMessage()
