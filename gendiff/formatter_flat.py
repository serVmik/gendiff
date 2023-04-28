from gendiff.gendiff_tools import create_lst_of_keys


def identify_change_of_line(key, dct1, dct2):
    if dct1.get(key) == dct2.get(key):
        return 'equal'

    elif key in dct1 and key in dct2:
        return 'changed'

    elif key in dct1:
        return 'removed'

    return 'added'


def parse_flat(dct_from_file1, dct_from_file2):
    lst_of_diff = create_lst_of_keys(dct_from_file1, dct_from_file2)

    for index, key in enumerate(lst_of_diff):
        lst_of_diff[index] = (
            key,
            identify_change_of_line(key, dct_from_file1, dct_from_file2)
        )

    return lst_of_diff
