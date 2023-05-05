from gendiff.formatters.output_stylish import create_output_stylish
from tests.fixtures import expected_parse_stylish


def test_create_output_stylish():
    with open('tests/fixtures/expected_output_stylish.txt', 'r') as expected:
        assert create_output_stylish(
            expected_parse_stylish.dct1,
            expected_parse_stylish.dct2,
            expected_parse_stylish.lst_of_diff
        ) == expected.read()
