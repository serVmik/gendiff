import pytest
from gendiff.formatter_stylish import create_lst_of_keys_stylish
from gendiff.gendiff_tools import get_dct_from_file
from tests.fixtures.expected_in_lst_of_diff_stylish import lst_of_diff


@pytest.mark.parametrize("file1, file2", [
    ('tests/fixtures/file1_for_test_stylish.json',
     'tests/fixtures/file2_for_test_stylish.json')
])
def test_create_lst_of_keys_stylish(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)
    assert create_lst_of_keys_stylish(
        dct_from_file1, dct_from_file2) == lst_of_diff
