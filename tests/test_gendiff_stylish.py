# import pytest
# from gendiff.output_diff_stylish import make_lines
# from tests.fixtures.expected_in_lst_of_diff_stylish import lst_of_diff
# from gendiff.gendiff_tools import get_dct_from_file
#
#
# @pytest.mark.parametrize("file1, file2", [
#     ('tests/fixtures/file1_for_test_stylish.json',
#      'tests/fixtures/file1_for_test_stylish.json')
# ])
# def test_create_a_string_of_diff(file1, file2):
#     dct1 = get_dct_from_file(file1)
#     dct2 = get_dct_from_file(file2)
#     with open('tests/fixtures/expected_from_test_stylish', 'r') as expected:
#         assert make_lines(dct1, dct2, lst_of_diff) == expected.read()
