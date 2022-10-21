'''This module does HTTP requests settings and error handling.'''

from functools import wraps
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

from apis.exceptions import exc


DEFAULT_TIMEOUT = 5  # seconds
DEFAULT_RETRIES = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS']
)


class TimeoutHTTPAdapter(HTTPAdapter):
    '''Set up HTTP requests timeouts and retries.'''

    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        self.max_retries = DEFAULT_RETRIES

        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
            del kwargs['timeout']

        if 'max_retries' in kwargs:
            self.max_retries = kwargs['max_retries']
            del kwargs['max_retries']

        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get('timeout')

        if timeout is None:
            kwargs['timeout'] = self.timeout

        return super().send(request, **kwargs)


def error_handler(func):
    '''Decorator that displays try/except errors from the HTTP requests.'''

    @wraps(func)
    def wrapper(*args, **kwargs):  # pylint: disable=[R1710]
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            print(f'{exc.RED} - HTTP Request: {e}{exc.CLOSE_ASCII}')
        except requests.exceptions.ConnectionError as e:
            print(f'{exc.RED} - Connection: {e}{exc.CLOSE_ASCII}')
        except requests.exceptions.Timeout as e:
            print(f'{exc.RED} - Timeout: {e}{exc.CLOSE_ASCII}')
        except requests.exceptions.RetryError as e:
            print(f'{exc.RED} - Max Retries: {e}{exc.CLOSE_ASCII}')
        except requests.exceptions.RequestException as e:
            print(f'{exc.RED} - Something Else: {e}{exc.CLOSE_ASCII}')
    return wrapper
