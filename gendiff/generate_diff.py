from gendiff.create_diff import create_diff
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_json import format_json
import json
import yaml
import os


def parse_data(data, extension):
    if extension == '.json':
        return json.load(data)
    elif extension == '.yml' or extension == '.yaml':
        return yaml.safe_load(data)
    raise Exception('Unsupported file format entered!')


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as data:
        return parse_data(data, extension)


def generate_diff(file_path1, file_path2, format_='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = create_diff(data1, data2)

    match format_:
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
        case 'json':
            return format_json(diff)
