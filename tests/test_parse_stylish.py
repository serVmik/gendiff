from gendiff.parse_stylish import parse_stylish
from tests.fixtures import expected_parse_stylish


def test_parse_stylish():
    assert parse_stylish(
        expected_parse_stylish.dct1,
        expected_parse_stylish.dct2
    ) == expected_parse_stylish.lst_of_diff
