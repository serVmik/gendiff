from gendiff.create_differences import create_differences
from gendiff.formatters.format_stylish import display_in_format_stylish
from gendiff.formatters.format_plain import display_in_format_plain
from gendiff.formatters.format_json import display_in_format_json
import json
import yaml
import os


def get_dict_from_file(filepath):
    extension = os.path.splitext(filepath)[-1].lstrip('.')

    with open(filepath) as input_filepath:
        if extension == 'json':
            return json.load(input_filepath)

        elif extension == 'yml' or extension == 'yaml':
            return yaml.safe_load(input_filepath)

    raise Exception('Unsupported file format entered!')


def generate_diff(filepath1, filepath2, format='stylish'):
    dict_from_file1 = get_dict_from_file(filepath1)
    dict_from_file2 = get_dict_from_file(filepath2)
    differences = create_differences(dict_from_file1, dict_from_file2)

    match format:
        case 'stylish':
            return display_in_format_stylish(differences)
        case 'plain':
            return display_in_format_plain(differences)
        case 'json':
            return display_in_format_json(differences)
