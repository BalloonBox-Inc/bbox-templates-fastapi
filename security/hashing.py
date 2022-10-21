''' This module manages encryption authentication.'''

import hashlib
import hmac

from config import settings


def generate_hash(text: str):
    '''Encript a string with SHA3-512 algorithm.'''
    key = settings.SECURITY.JWT_SECRET_KEY.encode('utf-8')
    return hmac.new(key=key, msg=text.encode('utf-8'), digestmod=hashlib.sha3_512).hexdigest()


def verify_hash(signature: str, hash: str):
    '''Check if string-signature is valid.'''
    return bool(hash == generate_hash(signature))
