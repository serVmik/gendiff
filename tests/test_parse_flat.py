from gendiff.parse_flat import parse_flat
from tests.fixtures import expected_parse_flat


def test_parse_flat():
    assert parse_flat(
        expected_parse_flat.dct1,
        expected_parse_flat.dct2
    ) == expected_parse_flat.lst_of_diff
