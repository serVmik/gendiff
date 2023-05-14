from gendiff.parse_plain import parse_plain
from tests.fixtures import expected_parser_plain


def test_parse_plain():
    assert parse_plain(
        expected_parser_plain.dct1,
        expected_parser_plain.dct2
    ) == expected_parser_plain.lst_dcts_of_diff
