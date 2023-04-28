from gendiff.gendiff_tools import get_dct_from_file
from gendiff.formatter_flat import parse_flat
from gendiff.output_diff_flat import create_a_string_of_diff


def generate_gendiff(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)

    lst_of_diff = parse_flat(dct_from_file1, dct_from_file2)

    result_string = create_a_string_of_diff(
        dct_from_file1, dct_from_file2, lst_of_diff
        )

    return result_string
