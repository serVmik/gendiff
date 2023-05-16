from gendiff.formatters import output_plain
from tests.fixtures import expected_parser


def test_create_output_plain():
    with open('tests/fixtures/expected_output_plain.txt', 'r') as expected:
        assert output_plain.create_output_plain(
            expected_parser.dct1,
            expected_parser.dct2,
            expected_parser.lst_dcts_of_diff
        ) == expected.read()
