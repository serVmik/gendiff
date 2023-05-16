from gendiff.formatters import output_stylish
from tests.fixtures import expected_parser


def test_create_output_stylish():
    with open('tests/fixtures/expected_output_stylish.txt', 'r') as expected:
        assert output_stylish.create_output_stylish(
            expected_parser.dct1,
            expected_parser.dct2,
            expected_parser.lst_dcts_of_diff
        ) == expected.read()
