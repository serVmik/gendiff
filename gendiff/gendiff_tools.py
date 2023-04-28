import json
import yaml


def create_lst_of_keys(dct1, dct2):
    return sorted(list(set(dct1.keys()).union(dct2.keys())))


def get_dct_from_file(file):
    type_of_file = file[-file[::-1].find('.'):]

    if type_of_file == 'json':
        return json.load(open(file))

    elif type_of_file == 'yml' or type_of_file == 'yaml':
        return yaml.safe_load(open(file, 'r'))

    else:
        raise Exception('Unsupported file format entered!')
