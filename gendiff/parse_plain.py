from gendiff.gendiff_tools import create_lst_of_keys
from gendiff.gendiff_tools import make_marker_for_diff


def create_lst_dcts_of_diff(lst_of_diff):
    lst_dct_of_diff = list(map(
        lambda element: {'property': element},
        lst_of_diff
    ))
    return lst_dct_of_diff


def add_nesting_to_lst_dcts_of_diff(key, dct1, dct2, dct):
    if isinstance(dct1.get(key), dict) and isinstance(dct2.get(key), dict):
        dct['nested'] = parse_plain(dct1[key], dct2[key])

    elif isinstance(dct1.get(key), dict):
        dct['nested'] = parse_plain(dct1[key], dct1[key])

    elif isinstance(dct2.get(key), dict):
        dct['nested'] = parse_plain(dct2[key], dct2[key])


def complete_lst_dcts_of_diff(dct1, dct2, lst_dcts_of_diff):
    for dct in lst_dcts_of_diff:
        key = dct.get('property')
        dct['marker'] = make_marker_for_diff(key, dct1, dct2)
        add_nesting_to_lst_dcts_of_diff(key, dct1, dct2, dct)

    return lst_dcts_of_diff


def parse_plain(dct1, dct2):
    lst_of_keys = create_lst_of_keys(dct1, dct2)
    lst_dcts_of_diff = create_lst_dcts_of_diff(lst_of_keys)
    complete_lst_dcts_of_diff(dct1, dct2, lst_dcts_of_diff)

    return lst_dcts_of_diff
