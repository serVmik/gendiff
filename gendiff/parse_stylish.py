from gendiff.gendiff_tools import create_lst_of_keys
from gendiff.gendiff_tools import make_marker_for_diff


def add_marker_to_lst_of_diff(index_of_lst, value1, value2, lst_of_diff):
    lst_of_diff[index_of_lst].append(parse_stylish(value1, value2))


def complete_the_lst(dct1, dct2, lst_of_diff):
    for index, key in enumerate(lst_of_diff):
        lst_of_diff[index] = [key, make_marker_for_diff(key, dct1, dct2)]

        if isinstance(dct1.get(key), dict) and isinstance(dct2.get(key), dict):
            add_marker_to_lst_of_diff(index, dct1[key], dct2[key], lst_of_diff)

        elif isinstance(dct1.get(key), dict):
            add_marker_to_lst_of_diff(index, dct1[key], dct1[key], lst_of_diff)

        elif isinstance(dct2.get(key), dict):
            add_marker_to_lst_of_diff(index, dct2[key], dct2[key], lst_of_diff)

    return lst_of_diff


def parse_stylish(dct1, dct2):
    lst_of_diff = create_lst_of_keys(dct1, dct2)
    complete_the_lst(dct1, dct2, lst_of_diff)

    return lst_of_diff
