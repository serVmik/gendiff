from gendiff.gendiff_tools import create_lst_of_keys


def create_lst_dcts_of_diff(lst_of_diff):
    lst_dct_of_diff = list(map(
        lambda element: {'property': element},
        lst_of_diff
    ))
    return lst_dct_of_diff


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


def add_marker_to_lst_of_diff(value1, value2, dct):
    dct['nested'] = parse_plain(value1, value2)


def complete_the_lst(dct1, dct2, lst_dcts_of_diff):
    for dct in lst_dcts_of_diff:
        key = dct.get('property')
        dct['marker'] = make_marker_for_diff(key, dct1, dct2)

        if isinstance(dct1.get(key), dict) \
                and isinstance(dct2.get(key), dict):
            add_marker_to_lst_of_diff(
                dct1[key], dct2[key], dct
            )
        elif isinstance(dct1.get(key), dict):
            add_marker_to_lst_of_diff(
                dct1[key], dct1[key], dct
            )
        elif isinstance(dct2.get(key), dict):
            add_marker_to_lst_of_diff(
                dct2[key], dct2[key], dct
            )

    return lst_dcts_of_diff


def parse_plain(dct1, dct2):
    lst_of_diff = create_lst_of_keys(dct1, dct2)
    lst_dcts_of_diff = create_lst_dcts_of_diff(lst_of_diff)
    complete_the_lst(dct1, dct2, lst_dcts_of_diff)

    return lst_dcts_of_diff
