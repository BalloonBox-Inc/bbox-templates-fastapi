'''This module configures application settings from config.yaml'''

from pyaml_env import parse_config
from dotenv import load_dotenv

from helpers.misc import format_db_url


load_dotenv()


class Settings():
    '''Project settings.'''

    def __init__(self, d):
        for k, v in d.items():
            if isinstance(k, (list, tuple)):
                setattr(self, k, [Settings(x) if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, Settings(v) if isinstance(v, dict) else v)


# project settings
config = parse_config('config.yaml')

# set up environment
env = config['APP']['ENVIRONMENT']
if env == 'development':
    config['APP']['DEBUG'] = True
    config['APP']['TESTING'] = True

# format database URL
config['DATABASE']['BASE_URL'] = format_db_url(config['DATABASE']['BASE_URL'])

# dict to class
settings = Settings(config)
