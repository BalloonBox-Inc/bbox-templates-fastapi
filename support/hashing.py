from helpers.support_files import read_env_vars
import hashlib
import hmac


def encrypt_password(password):
    return hmac.new(key=read_env_vars('JWT_SECRET_KEY').encode('utf-8'), msg=password.encode('utf-8'), digestmod=hashlib.sha3_512).hexdigest()


def verify_password(plain_password, hashed_password):
    return True if hashed_password == encrypt_password(plain_password) else False
