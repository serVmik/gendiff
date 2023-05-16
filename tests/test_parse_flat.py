from gendiff import parser
from tests.fixtures import expected_parse_flat


def test_parse_flat():
    assert parser.parse_plain(
        expected_parse_flat.dct1,
        expected_parse_flat.dct2
    ) == expected_parse_flat.lst_dcts_of_diff
