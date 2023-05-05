import pytest
from gendiff.gendiff_parser import generate_gendiff


@pytest.mark.parametrize("file1, file2", [
    ('tests/fixtures/file1_flat.json',
     'tests/fixtures/file2_flat.json'),
    ('tests/fixtures/file1_flat.yaml',
     'tests/fixtures/file2_flat.yml')
])
def test_gendiff(file1, file2):
    with open(
            'tests/fixtures/expected_output_flat.txt', 'r'
    ) as expected:
        assert generate_gendiff(file1, file2) == expected.read()
