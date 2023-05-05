from tests.fixtures import expected_parse_flat
from gendiff.formatters.output_flat import create_output_flat


def test_create_lines_flat():
    with open('tests/fixtures/expected_output_flat.txt', 'r') as expected:
        assert create_output_flat(
            expected_parse_flat.dct1,
            expected_parse_flat.dct2,
            expected_parse_flat.lst_of_diff
        ) == expected.read()
