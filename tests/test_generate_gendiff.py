import pytest
import gendiff.gendiff_module
import gendiff.gendiff_parser

file1_json_for_test = 'tests/fixtures/file1_for_test.json'
file2_json_for_test = 'tests/fixtures/file2_for_test.json'


@pytest.mark.parametrize("file1, file2", [
    (file1_json_for_test, file2_json_for_test)
])


def test_gendiff(file1, file2):
    with open('tests/fixtures/expected_from_test_file1_file2.txt', 'r') as expected:
        function_for_test = gendiff.gendiff_module.generate_gendiff(
            file1_json_for_test, file2_json_for_test
            )
        assert function_for_test == expected.read()
