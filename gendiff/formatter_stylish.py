from gendiff.gendiff_tools import get_dct_from_file


def create_lst_of_keys_stylish(dct1, dct2):
    lst_of_diff_stylish = sorted(list(set(dct1.keys()).union(dct2.keys())))
    # lst_of_diff_stylish = []
    return lst_of_diff_stylish


def identify_change_of_line(key, dct1, dct2):
    if dct1.get(key) == dct2.get(key):
        return 'equal'

    elif key in dct1 and key in dct2:
        return 'changed'

    elif key in dct1:
        return 'removed'

    return 'added'


def parse_flat(dct_from_file1, dct_from_file2):
    lst_of_diff_stylish = create_lst_of_keys_stylish(
        dct_from_file1, dct_from_file2
    )

    for index, key in enumerate(lst_of_diff_stylish):
        lst_of_diff_stylish[index] = (
            key,
            identify_change_of_line(key, dct_from_file1, dct_from_file2)
        )

    print(lst_of_diff_stylish)

    return lst_of_diff_stylish


def generate_gendiff(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)

    lst_of_diff = parse_flat(dct_from_file1, dct_from_file2)

    # result_string = create_lst_of_keys_stylish(
    #     dct_from_file1, dct_from_file2, lst_of_diff
    #     )

    # return result_string


# generate_gendiff('../for_developer/file1.json', '../for_developer/file2.json')
