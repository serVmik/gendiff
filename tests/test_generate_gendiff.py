import pytest
from gendiff.display_in_format import generate_diff


@pytest.mark.parametrize("file1, file2, expected_txt, format", [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_json.txt',
     'json'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_plain.txt',
     'plain'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_stylish.txt',
     'stylish')])
def test_gendiff_use_format(file1, file2, expected_txt, format):
    with open(expected_txt, 'r') as expected:
        assert generate_diff(file1, file2, format) == expected.read()


@pytest.mark.parametrize("file1, file2, expected_txt, format", [
    ('tests/fixtures/file1.txt',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_stylish.txt',
     'stylish')])
def test_get_dict_from_file_on_exception(file1, file2, expected_txt, format):
    with pytest.raises(Exception):
        with open(expected_txt, 'r') as expected:
            assert generate_diff(file1, file2, format) == expected.read()
