'''This module contains a miscellaneous collection of unit functions.'''

import json
import time


# Time
def current_utc_timestamp():
    '''Get current timestamp at UTC.'''
    return int(time.time())


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


def flatten_list(lst: list):
    '''Flat list out of a list of lists.'''
    return [item for sublist in lst for item in sublist]


# Managing files
def read_txt(filename: str):
    '''Read a text file.'''
    with open(filename, mode='r', encoding='utf-8') as f:
        return f.read()


def read_json(filename: str):
    '''Read a JSON file.'''
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
