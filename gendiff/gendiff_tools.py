import json
import yaml


def get_dct_from_file(file):
    type_of_file = file[-file[::-1].find('.'):]

    if type_of_file == 'json':
        return json.load(open(file))

    elif type_of_file == 'yml' or type_of_file == 'yaml':
        return yaml.safe_load(open(file, 'r'))

    else:
        raise Exception('Unsupported file format entered!')


def make_marker_if_changed(dct1, dct2, key):
    if isinstance(dct1.get(key), dict) and isinstance(dct2.get(key), dict):
        return 'without_marker'
    else:
        return 'changed'


def make_marker_for_diff(key, dct1, dct2):
    if dct1.get(key) == dct2.get(key):
        result = 'equal'

    elif key in dct1 and key in dct2:
        result = make_marker_if_changed(dct1, dct2, key)

    elif key in dct1:
        result = 'removed'

    else:
        # key in dct2:
        result = 'added'

    return result
