# import pytest
# from gendiff.gendiff_module import parse_only_lines
# from gendiff.gendiff_get_from_file import get_dct_from_file
# from tests.fixtures.expected_in_lst_of_diff import lst_of_diff


# @pytest.mark.parametrize("file1, file2", [
#     ('tests/fixtures/file1_for_test_stylich.json',
#      'tests/fixtures/file2_for_test_stylich.json')
# ])
# def test_create_lst_of_actions(file1, file2):
#     dct_from_file1 = get_dct_from_file(file1)
#     dct_from_file2 = get_dct_from_file(file2)
#     assert parse_only_lines(
#         dct_from_file1, dct_from_file2) == lst_of_diff
