'''This module contains a miscellaneous collection of unit functions.'''

import json


# Data type convertion
def string_to_list(string: str, sep=','):
    '''Convert string to list.'''
    return string.split(sep)


# Formatting
def format_db_url(url: str):
    '''Format Postgres URL string.'''
    if 'postgresql' not in url:
        url = url.replace('postgres', 'postgresql')
    return url


def objects_to_dict_list(lst: list):
    '''Convert a list of objects to a list of dict'''
    return [item.__dict__ for item in lst]


# Managing files
def read_txt(filename: str):
    '''Read a text file.'''
    with open(filename, mode='r', encoding='utf-8') as f:
        return f.read()


def read_json(filename: str):
    '''Read a JSON file.'''
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)


# Calling functions
def try_except(func, *args, **kwargs):
    '''Generic try-except function.'''
    try:
        return func(*args, **kwargs)
    except Exception as e:  # noqa: F841 pylint: disable=[W0612,W0703]
        return None
