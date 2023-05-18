from gendiff.gendiff_tools import get_dct_from_file
from gendiff.parser import parse_plain
from gendiff.formatters.output_stylish import create_output_stylish
from gendiff.formatters.output_plain import create_output_plain
from gendiff.formatters.output_json import create_output_json


def generate_gendiff(file1, file2, format='stylish'):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)
    lst_dcts_of_diff = parse_plain(dct_from_file1, dct_from_file2)

    match format:
        case 'stylish':
            result_string = create_output_stylish(
                dct_from_file1, dct_from_file2, lst_dcts_of_diff
            )
        case 'plain':
            result_string = create_output_plain(
                dct_from_file1, dct_from_file2, lst_dcts_of_diff
            )
        case 'json':
            result_string = create_output_json(
                lst_dcts_of_diff
            )
        case _:
            raise Exception('Unsupported format entered!')

    return result_string
