from os.path import dirname, join
from pandas import read_csv
from json import load


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

        if ext == '.csv':
            return read_csv(file)

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
