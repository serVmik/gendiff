import pytest
import gendiff.gendiff_module as gendiff_

file1_json = 'tests/fixtures/file1_for_test.json'
file2_json = 'tests/fixtures/file2_for_test.json'
file1_yaml = 'tests/fixtures/file1_for_test.yaml'
file2_yml = 'tests/fixtures/file2_for_test.yml'


@pytest.mark.parametrize("file1, file2", [
    (file1_json, file2_json), (file1_yaml, file2_yml)
])
def test_gendiff(file1, file2):
    with open('tests/fixtures/expected_from_test_file1_file2.txt', 'r') as expected:
        assert gendiff_.generate_gendiff(file1, file2) == expected.read()
