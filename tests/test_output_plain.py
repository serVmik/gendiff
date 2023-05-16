from gendiff.formatters.output_plain import create_output_plain
from tests.fixtures import expected_parser_plain


def test_create_output_plain():
    with open('tests/fixtures/expected_output_plain.txt', 'r') as expected:
        assert create_output_plain(
            expected_parser_plain.dct1,
            expected_parser_plain.dct2,
            expected_parser_plain.lst_dcts_of_diff
        ) == expected.read()
