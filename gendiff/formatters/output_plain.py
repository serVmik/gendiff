from gendiff.gendiff_tools import create_quote_for_string
from gendiff.gendiff_tools import convert_to_string
from gendiff.gendiff_tools import get_value_using_path


def create_line_with_changed(dct1, dct2, path, lst_dcts_of_diff):
    value2 = convert_to_string(get_value_using_path(dct2, path))
    quote2 = create_quote_for_string(value2)
    value1 = convert_to_string(get_value_using_path(dct1, path))
    quote1 = create_quote_for_string(value1)

    if 'nested' in lst_dcts_of_diff:
        if not isinstance(value1, dict):
            return f"Property '{'.'.join(path)}' was updated. " \
                   f"From [complex value] to {quote2}{value2}{quote2}"
        else:
            return f"Property '{'.'.join(path)}' was updated. " \
                   f"From {quote1}{value1}{quote1} to [complex value]"
    else:
        return f"Property '{'.'.join(path)}' was updated. "\
               f"From {quote1}{value1}{quote1} to {quote2}{value2}{quote2}"


def create_line_with_added(dct2, path, lst_dcts_of_diff):
    value2 = convert_to_string(get_value_using_path(dct2, path))
    quote2 = create_quote_for_string(value2)

    if 'nested' in lst_dcts_of_diff:
        return f"Property '{'.'.join(path)}' was added with value: " \
               f"[complex value]"
    else:
        return f"Property '{'.'.join(path)}' was added with value: " \
               f"{quote2}{value2}{quote2}"


def create_output_plain(dct1, dct2, lst_dcts_of_diff_input):
    lst_of_lines = []

    def walk(lst_dcts_of_diff, path):
        path += (lst_dcts_of_diff.get('property'),)
        marker = lst_dcts_of_diff.get('marker')

        if marker == 'added':
            lst_of_lines.append(
                create_line_with_added(dct2, path, lst_dcts_of_diff)
            )
        elif marker == 'changed':
            lst_of_lines.append(
                create_line_with_changed(dct1, dct2, path, lst_dcts_of_diff)
            )
        elif marker == 'removed':
            lst_of_lines.append(f"Property '{'.'.join(path)}' was removed")

        list(map(
            lambda item: walk(item, path),
            lst_dcts_of_diff.get('nested', [])
        ))

    for element in lst_dcts_of_diff_input:
        walk(element, ())

    return '\n'.join(lst_of_lines)
