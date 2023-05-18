def convert_to_str(value):
    if isinstance(value, str):
        return f"'{value}'"

    elif value in (True, False, None):
        return str(value).\
            replace('True', 'true').\
            replace('False', 'false').\
            replace('None', 'null')


def get_value_using_path(dct_input, path_input):
    received_value = []

    def walk(dct, path, index):
        key = path[index]
        value = dct.get(key)

        if len(path) > index + 1:
            walk(value, path, index + 1)

        received_value.append(value)

    walk(dct_input, path_input, 0)
    return received_value[0]


def create_line_with_changed(value1, value2, path):
    if isinstance(value1, dict):
        return f"Property '{'.'.join(path)}' was updated. " \
               f"From [complex value] to {convert_to_str(value2)}"

    elif isinstance(value2, dict):
        return f"Property '{'.'.join(path)}' was updated. " \
               f"From {convert_to_str(value1)} to [complex value]"

    else:
        return f"Property '{'.'.join(path)}' was updated. "\
               f"From {convert_to_str(value1)} to {convert_to_str(value2)}"


def create_line_with_added(dct2, path, lst_dcts_of_diff):
    if 'nested' in lst_dcts_of_diff:
        return f"Property '{'.'.join(path)}' was added with value: " \
               f"[complex value]"
    else:
        value2 = get_value_using_path(dct2, path)
        return f"Property '{'.'.join(path)}' was added with value: " \
               f"{convert_to_str(value2)}"


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
            value1 = get_value_using_path(dct1, path)
            value2 = get_value_using_path(dct2, path)
            lst_of_lines.append(
                create_line_with_changed(value1, value2, path)
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
