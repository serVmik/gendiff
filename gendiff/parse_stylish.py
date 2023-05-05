from gendiff.gendiff_tools import create_lst_of_keys


def make_marker_if_changed(dct1, dct2, key):
    if isinstance(dct1.get(key), dict)\
            and not isinstance(dct2.get(key), dict):
        return 'changed'
    if isinstance(dct1.get(key), dict):
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


def add_marker_to_lst_of_diff(index_of_lst, value1, value2, lst_of_diff):
    lst_of_diff[index_of_lst].append(
        parse_stylish(value1, value2)
    )


def complete_the_lst(dct1, dct2, lst_of_diff):
    for index, key in enumerate(lst_of_diff):
        lst_of_diff[index] = [
            key,
            make_marker_for_diff(key, dct1, dct2)
        ]

        if isinstance(dct1.get(key), dict) \
                and isinstance(dct2.get(key), dict):
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
