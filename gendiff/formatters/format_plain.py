def convert_to_str(value):
    if isinstance(value, dict):
        converted_value = '[complex value]'
    elif isinstance(value, str):
        converted_value = f"'{value}'"
    elif isinstance(value, bool):
        converted_value = str(value).lower()
    elif value is None:
        converted_value = 'null'
    else:
        return value

    return converted_value


def create_lines(diff, lines, path):
    path += (diff.get('property'),)
    status = diff.get('status')

    list(map(lambda item: create_lines(item, lines, path),
             diff.get('nested', [])))

    if status == 'added':
        lines.append(f"Property '{'.'.join(path)}' was added with value: "
                     f"{convert_to_str(diff.get('new_value'))}")
    elif status == 'updated':
        lines.append(f"Property '{'.'.join(path)}' was updated. "
                     f"From {convert_to_str(diff.get('old_value'))} "
                     f"to {convert_to_str(diff.get('new_value'))}")
    elif status == 'removed':
        lines.append(f"Property '{'.'.join(path)}' was removed")

    return '\n'.join(lines)


def format_plain(diff):
    result = []

    for element in diff:
        result.append(create_lines(element, [], ()))

    return '\n'.join(result)
