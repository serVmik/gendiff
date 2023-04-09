import gendiff.gendiff_module
import gendiff.gendiff_parser

file1_json_for_test = 'tests/fixtures/file1_for_test.json'
file2_json_for_test = 'tests/fixtures/file2_for_test.json'


def test_gendiff():
    expected = open('tests/fixtures/expected_from_test_file1_file2.txt', 'r').read()
    function_for_test = gendiff.gendiff_module.generate_gendiff(
        file1_json_for_test, file2_json_for_test
        )
    assert function_for_test == expected
