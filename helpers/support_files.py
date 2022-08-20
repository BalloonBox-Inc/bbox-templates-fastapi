from os.path import dirname
from os.path import join
from os import getenv
from dotenv import load_dotenv
from json import load
load_dotenv()


def read_env_vars(var):
    return getenv(var)


def get_root():
    return dirname(__file__).replace('/helpers', '')


def read_file(filename):
    try:
        file = join(get_root(), f'{filename}')
        ext = filename.split('.')[-1]

        if ext == 'json':
            with open(file) as f:
                data = load(f)
            return data

    except Exception as e:
        print(f'\033[31m ERROR: {e}\033[0m')
        return False


def write_file(filename, content):
    try:
        file = join(get_root(), f'{filename}')
        with open(file, 'w') as f:
            f.write(content)
        return True

    except Exception as e:
        print(f'\033[31m ERROR: {e}\033[0m')
        return False
