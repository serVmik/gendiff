from gendiff.gendiff_tools import add_quote_to_string
from gendiff.gendiff_tools import convert_to_string
from gendiff.gendiff_tools import get_value_using_path


def create_output_plain(dct1_input, dct2_input, lst_of_diff):
    lst_of_lines = []

    def walk(node, path):
        path += (node.get('property'),)
        action = node.get('marker')

        if 'nested' not in node and action == 'added':
            value2 = convert_to_string(get_value_using_path(dct2_input, path))
            quote = add_quote_to_string(value2)

            line = f"Property '{'.'.join(path)}' was added with value: " \
                   f"{quote}{value2}{quote}"
            lst_of_lines.append(line)

        elif action == 'added':
            line = f"Property '{'.'.join(path)}' was added with value: " \
                   f"[complex value]"
            lst_of_lines.append(line)

        elif 'nested' not in node and action == 'changed':
            value1 = convert_to_string(get_value_using_path(dct1_input, path))
            quote1 = add_quote_to_string(value1)
            value2 = convert_to_string(get_value_using_path(dct2_input, path))
            quote2 = add_quote_to_string(value2)

            line = f"Property '{'.'.join(path)}' was updated. " \
                   f"From {quote1}{value1}{quote1} to {quote2}{value2}{quote2}"
            lst_of_lines.append(line)

        elif action == 'changed':
            value2 = convert_to_string(get_value_using_path(dct2_input, path))
            quote = add_quote_to_string(value2)

            line = f"Property '{'.'.join(path)}' was updated. " \
                   f"From [complex value] to {quote}{value2}{quote}"
            lst_of_lines.append(line)

        elif action == 'removed':
            line = f"Property '{'.'.join(path)}' was removed"
            lst_of_lines.append(line)

        lst_of_nested_property = node.get('nested', [])
        list(map(
            lambda item: walk(item, path),
            lst_of_nested_property
        ))

    for element in lst_of_diff:
        walk(element, ())

    return '\n'.join(lst_of_lines)
