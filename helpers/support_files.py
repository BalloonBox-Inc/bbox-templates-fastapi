from os.path import dirname
from os.path import join
from os import getenv
from json import load
from dotenv import load_dotenv
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
            with open(file, encoding='utf-8') as f:
                data = load(f)
            return data
        return None

    except OSError as e:
        print(f'\033[31m ERROR: {e}\033[0m')
        return None


def write_file(filename, content):
    try:
        file = join(get_root(), f'{filename}')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    except OSError as e:
        print(f'\033[31m ERROR: {e}\033[0m')
        return False
