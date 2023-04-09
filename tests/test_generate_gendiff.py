import pytest
from gendiff.gendiff_module import generate_gendiff


@pytest.mark.parametrize("file1, file2", [
    ('tests/fixtures/file1_for_test.json', 'tests/fixtures/file2_for_test.json'),
    ('tests/fixtures/file1_for_test.yaml', 'tests/fixtures/file2_for_test.yml')
])
def test_gendiff(file1, file2):
    with open('tests/fixtures/expected_from_test_file1_file2.txt', 'r') as expected:
        assert generate_gendiff(file1, file2) == expected.read()
