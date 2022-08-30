from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Settings:

    # project
    PROJECT_NAME = 'YourProjectName'
    PROJECT_VERSION = '1.0.0'

    # database
    DATABASE_URI = getenv('DATABASE_URI')
    if 'postgresql' not in DATABASE_URI:
        DATABASE_URI = DATABASE_URI.replace('postgres', 'postgresql')

    # security
    ACCESS_TOKEN_EXPIRE_MINUTES = getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    JWT_ALGORITHM = getenv('JWT_ALGORITHM')
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')

    # testing
    TEST_USER_EMAIL = 'test@example.com'
    TEST_USER_PASSWORD = 'super-secret-password'
    TEST_USER_STATUS = False


settings = Settings()
