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


def create_lines(diff, path_traveled=None):
    path_traveled = [] if path_traveled is None else path_traveled
    lines = []

    for property_ in diff:
        status = property_.get('status')
        path = path_traveled + [property_.get('property')]

        if status == 'added':
            lines.append(f"Property '{'.'.join(path)}' was added with value: "
                         f"{convert_to_str(property_.get('new_value'))}")
        elif status == 'updated':
            lines.append(f"Property '{'.'.join(path)}' was updated. "
                         f"From {convert_to_str(property_.get('old_value'))} "
                         f"to {convert_to_str(property_.get('new_value'))}")
        elif status == 'removed':
            lines.append(f"Property '{'.'.join(path)}' was removed")
        elif status == 'nested':
            lines.extend(create_lines(property_.get('nested'), path))

    return lines


def format_plain(diff):
    return '\n'.join(create_lines(diff))
