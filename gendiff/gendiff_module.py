import json
import yaml
from gendiff.gendiff_parser import create_a_string_of_diff


def get_dct_from_file(file_):
    type_of_file = file_[-file_[::-1].find('.'):]
    dct_from_file = dict()

    if type_of_file == 'json':
        dct_from_file = json.load(open(file_))
    elif type_of_file == 'yml' or type_of_file == 'yaml':
        dct_from_file = yaml.safe_load(open(file_, 'r'))
    else:
        raise Exception('Unsupported file format entered!')

    return dct_from_file


def generate_gendiff(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)
    lst_of_keys = sorted(list(
        set(dct_from_file1.keys()).union(set(dct_from_file2.keys()))
    ))

    result_strings = '{\n'
    for key in lst_of_keys:
        result_strings += create_a_string_of_diff(
            dct_from_file1, dct_from_file2, key
        )
    result_strings += '}'

    return result_strings
