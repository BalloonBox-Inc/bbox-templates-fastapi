'''This module configures application settings from config.yaml'''

from helpers.lru_caching import timed_lru_cache
from pyaml_env import parse_config
from dotenv import load_dotenv

from helpers.app_settings import AppSettings
from helpers.misc import format_db_url


load_dotenv()


@timed_lru_cache(seconds=60)
def get_settings():
    '''Set up settings in cache for the above lifetime, then refreshes it.'''
    return AppSettings(config)


# project settings
config = parse_config('config.yaml')

# set up environment
env = config['APP']['ENVIRONMENT']
if env == 'development':
    config['APP']['DEBUG'] = True
    config['APP']['TESTING'] = True

# format database URL
config['DATABASE']['BASE_URL'] = format_db_url(config['DATABASE']['BASE_URL'])
