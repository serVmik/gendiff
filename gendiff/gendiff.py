import json


def load_json_object_in_dict(file_object):
    f = open('file_object')

    string_of_file = json.load(f)

    #read string by string

    f.close()

    return file_dict


def generate_gendiff(file_path1, file_path2):
    dict_for_diff_1 = load_json_object_in_dict(file_path1)
    dict_for_diff_2 = load_json_object_in_dict(file_path2)

    string_of_diff = f''

    return string_of_diff
