import hashlib
import hmac
from config import settings


def encrypt_password(password):
    key = settings.JWT_SECRET_KEY
    return hmac.new(key=key.encode('utf-8'), msg=password.encode('utf-8'), digestmod=hashlib.sha3_512).hexdigest()


def verify_password(plain_password, hashed_password):
    return bool(hashed_password == encrypt_password(plain_password))
