# import pytest
# from gendiff.output_diff_stylich import create_string_of_diff_stylish
# from gendiff.gendiff_tools import get_dct_from_file
# from tests.fixtures.expected_in_lst_of_diff import lst_of_diff
#
#
# @pytest.mark.parametrize('file1, file2', [
#     ('tests/fixtures/file1_for_test_stylish.json',
#      'tests/fixtures/file2_for_test_stylish.json')
# ])
# def test_create_string_of_diff_stylish(file1, file2):
#     dct_from_file1 = get_dct_from_file(file1)
#     dct_from_file2 = get_dct_from_file(file2)
#     expected = lst_of_diff
#     assert create_string_of_diff_stylish(
#         dct_from_file1, dct_from_file2, lst_of_diff) == expected
