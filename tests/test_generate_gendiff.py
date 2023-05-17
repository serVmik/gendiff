import pytest
from gendiff.gendiff_parser import generate_gendiff


@pytest.mark.parametrize("file1, file2, expected_txt, format", [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_stylish.txt',
     'stylish'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_plain.txt',
     'plain')
])
def test_gendiff(file1, file2, expected_txt, format):
    with open(expected_txt, 'r') as expected:
        assert generate_gendiff(file1, file2, format) == expected.read()
