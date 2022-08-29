from databases import Database
from config import settings


async def check_db_connected():
    try:
        db = Database(settings.DATABASE_URI)
        if not db.is_connected:
            await db.connect()
    except Exception as e:
        print(f'\033[31mERROR: \t  Unable to connect with database. {e}\033[0m')
        raise e


async def check_db_disconnected():
    try:
        db = Database(settings.DATABASE_URI)
        if db.is_connected:
            await db.disconnect()
    except Exception as e:
        print(f'\033[31mERROR: \t  Unable to disconnect from database. {e}\033[0m')
        raise e
