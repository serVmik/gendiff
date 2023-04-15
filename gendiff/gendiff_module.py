import json
import yaml
from gendiff.gendiff_parser import create_a_string_of_diff


def get_dct_from_file(file_):
    type_of_file = file_[-file_[::-1].find('.'):]

    if type_of_file == 'json':
        dct_from_file = json.load(open(file_))
    elif type_of_file == 'yml' or type_of_file == 'yaml':
        dct_from_file = yaml.safe_load(open(file_, 'r'))
    else:
        raise Exception('Unsupported file format entered!')

    return dct_from_file


def create_lst_of_actions(dct_from_file1, dct_from_file2):
    lst_of_actions_for_dct_key = sorted(list(
        set(dct_from_file1.keys()).union(dct_from_file2.keys())
    ))

    for index, key in enumerate(lst_of_actions_for_dct_key):
        if dct_from_file1.get(key) == dct_from_file2.get(key):
            lst_of_actions_for_dct_key[index] = (key, 'equal')
        elif key in dct_from_file1 and key in dct_from_file2:
            lst_of_actions_for_dct_key[index] = (key, 'changed')
        elif key in dct_from_file1:
            lst_of_actions_for_dct_key[index] = (key, 'removed')
        else:
            lst_of_actions_for_dct_key[index] = (key, 'added')

    return lst_of_actions_for_dct_key


def generate_gendiff(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)

    lst_of_actions_for_dct_key = create_lst_of_actions(
        dct_from_file1, dct_from_file2
    )
    result_string = create_a_string_of_diff(
        dct_from_file1, dct_from_file2, lst_of_actions_for_dct_key
    )

    return result_string
