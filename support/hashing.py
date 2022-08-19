from helpers.support_files import read_env_vars
from support import crud
import hashlib
import hmac


def encrypt_password(password):
    return hmac.new(key=read_env_vars('SECRET_KEY').encode('utf-8'), msg=password.encode('utf-8'), digestmod=hashlib.sha3_512).hexdigest()


def verify_password(plain_password, hashed_password):
    return True if hashed_password == encrypt_password(plain_password) else False


def authenticate_user(db, email, password):
    user = crud.get_user_by_email(db, email=email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
