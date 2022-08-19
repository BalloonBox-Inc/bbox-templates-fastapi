import hashlib
import hmac
from dotenv import load_dotenv
from os import getenv
load_dotenv()


def encrypt_password(password: str):
    return hmac.new(key=getenv('SECRET_KEY').encode('utf-8'), msg=password.encode('utf-8'), digestmod=hashlib.sha3_512).hexdigest()


def verify_password(hashed_password: str, password: str):
    return True if hashed_password == encrypt_password(password) else False
