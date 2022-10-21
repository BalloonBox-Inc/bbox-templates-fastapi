'''This module ensures that the database connection was safely established and terminated.'''

from databases import Database

from apis.exceptions import exc
from config import settings


async def check_db_connected():
    '''Ensure that the connection with the database has been established.'''
    try:
        db = Database(settings.DATABASE.BASE_URL)
        if not db.is_connected:
            await db.connect()
    except Exception as e:
        print(f'{exc.RED}: {exc.DB_CONNECT}{e}{exc.CLOSE_ASCII}')
        raise e


async def check_db_disconnected():
    '''Ensure that the connection with the database has been terminated.'''
    try:
        db = Database(settings.DATABASE.BASE_URL)
        if db.is_connected:
            await db.disconnect()
    except Exception as e:
        print(f'{exc.RED}: {exc.DB_DISCONNECT}{e}{exc.CLOSE_ASCII}')
        raise e
