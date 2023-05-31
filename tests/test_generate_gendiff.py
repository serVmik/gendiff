import pytest
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize("file_path1, file_path2, expected_txt, format", [
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
def test_generate_diff(file_path1, file_path2, expected_txt, format):
    with open(expected_txt, 'r') as expected:
        assert generate_diff(file_path1, file_path2, format) == expected.read()


@pytest.mark.parametrize("file_path1, file_path2, expected_txt, format", [
    ('tests/fixtures/file1.txt',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_output_stylish.txt',
     'stylish')])
def test_get_data_with_exception(
        file_path1, file_path2, expected_txt, format):
    with pytest.raises(Exception):
        with open(expected_txt, 'r') as expected:
            assert generate_diff(
                file_path1, file_path2, format) == expected.read()
