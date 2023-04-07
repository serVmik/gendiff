from gendiff.module_gendiff import generate_gendiff, create_a_string_of_diff

file1_json_for_test = 'fixtures/file1_for_test.json'
file2_json_for_test = 'fixtures/file2_for_test.json'


def test_gendiff():
    expected = open('fixtures/expected_from_test_file1_file2.txt', 'r').read()
    function_for_test = generate_gendiff(file1_json_for_test, file2_json_for_test)
    assert function_for_test == expected
