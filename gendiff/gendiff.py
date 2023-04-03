import json


def create_a_string_of_diff(dct1, dct2, key):
    if dct1.get(key) == dct2.get(key):
        return f'    {key}: {dct1[key]}\n'
    elif key in dct1 and key in dct2:
        return f'  - {key}: {dct1[key]}\n  + {key}: {dct2[key]}\n'
    elif key in dct1:
        return f'  - {key}: {dct1[key]}\n'
    else:
        return f'  + {key}: {dct2[key]}\n'


def generate_gendiff(file1, file2):
    dct_from_file1 = json.load(open(file1))
    dct_from_file2 = json.load(open(file2))

    lst_of_keys = list(set(
        list(dct_from_file1.keys()) + list(dct_from_file2.keys()))
        )
    lst_of_keys.sort()

    result_strings = '{\n'
    for key in lst_of_keys:
        string_of_diff = create_a_string_of_diff(
            dct_from_file1, dct_from_file2, key
            )
        result_strings += string_of_diff
    result_strings += '}'

    return result_strings
