from gendiff.create_diff import create_diff
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_json import format_json
import json
import yaml
import os


def get_data(file_path):
    _, extension = os.path.splitext(file_path)

    with open(file_path) as input_file_path:
        if extension == '.json':
            return json.load(input_file_path)

        elif extension == '.yml' or extension == '.yaml':
            return yaml.safe_load(input_file_path)

    raise Exception('Unsupported file format entered!')


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = create_diff(data1, data2)

    match format:
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
        case 'json':
            return format_json(diff)
