from gendiff.gendiff_tools import get_dct_from_file
from gendiff.parser import parse_diff
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_json import format_json


def generate_diff(file1, file2, format='stylish'):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)
    lst_dcts_of_diff = parse_diff(dct_from_file1, dct_from_file2)

    match format:
        case 'stylish':
            return format_stylish(
                dct_from_file1, dct_from_file2, lst_dcts_of_diff
            )
        case 'plain':
            return format_plain(
                dct_from_file1, dct_from_file2, lst_dcts_of_diff
            )
        case 'json':
            return format_json(lst_dcts_of_diff)
