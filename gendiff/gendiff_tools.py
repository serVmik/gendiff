import json
import yaml


def create_lst_of_keys(dct1, dct2):
    return sorted(list(set(dct1.keys()).union(dct2.keys())))


def get_value(node, key):
    return node.get(key) if isinstance(node, dict) else node


def get_value_using_path(dct_input, path_input):
    received_value = []
    start_index_of_key_along_path = 0

    def walk(dct, path, index):
        key = path[index]
        value = dct.get(key)

        if len(path) > 1 + index:
            walk(value, path, index + 1)

        received_value.append(value)

    walk(dct_input, path_input, start_index_of_key_along_path)
    return received_value[0]


def get_dct_from_file(file):
    type_of_file = file[-file[::-1].find('.'):]

    if type_of_file == 'json':
        return json.load(open(file))

    elif type_of_file == 'yml' or type_of_file == 'yaml':
        return yaml.safe_load(open(file, 'r'))

    else:
        raise Exception('Unsupported file format entered!')


def convert_to_string(value):
    return str(value).\
        replace('None', 'null').\
        replace('True', 'true').\
        replace('False', 'false')


def add_quote_to_string(value):
    return "" if value in ('true', 'false', 'null') else "'"


def make_marker_if_changed(dct1, dct2, key):
    if isinstance(dct1.get(key), dict) and not isinstance(dct2.get(key), dict):
        return 'changed'
    elif isinstance(dct1.get(key), dict):
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
