from gendiff.gendiff_tools import get_dct_from_file
from gendiff.parse_stylish import parse_stylish
from gendiff.parse_plain import parse_plain
from gendiff.formatters.output_stylish import create_output_stylish
from gendiff.formatters.output_plain import create_output_plain


def generate_gendiff(file1, file2, format='stylish'):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)

    match format:
        case 'stylish':
            lst_of_diff = parse_stylish(dct_from_file1, dct_from_file2)
            result_string = create_output_stylish(
                dct_from_file1, dct_from_file2, lst_of_diff
            )
        case 'plain':
            lst_dcts_of_diff = parse_plain(dct_from_file1, dct_from_file2)
            result_string = create_output_plain(
                dct_from_file1, dct_from_file2, lst_dcts_of_diff
            )
        case _:
            raise Exception('Unsupported format entered!')

    return result_string
