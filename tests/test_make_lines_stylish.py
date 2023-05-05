import pytest
from gendiff.output_diff_stylish import make_lines
from gendiff.gendiff_tools import get_dct_from_file
from tests.fixtures.expected_in_lst_of_diff_stylish import lst_of_diff


@pytest.mark.parametrize('file1, file2', [
    ('tests/fixtures/file1_for_test_stylish.json',
     'tests/fixtures/file2_for_test_stylish.json')
])
def test_make_lines(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)
    with open('tests/fixtures/expected_from_test_stylish.txt', 'r') as expected:
        assert make_lines(
            dct_from_file1, dct_from_file2, lst_of_diff) == expected.read()
