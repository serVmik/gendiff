def convert_to_str(value):
    if isinstance(value, str):
        return f"'{value}'"

    elif isinstance(value, dict):
        return '[complex value]'

    return str(value).\
        replace('True', 'true').\
        replace('False', 'false').\
        replace('None', 'null')


def format_plain(diff_input):
    lines = []

    def walk(diff, path):
        path += (diff.get('property'),)
        status = diff.get('status')

        if status == 'added':
            lines.append(f"Property '{'.'.join(path)}' was added with value: "
                         f"{convert_to_str(diff.get('new_value'))}")

        elif status == 'updated':
            lines.append(f"Property '{'.'.join(path)}' was updated. "
                         f"From {convert_to_str(diff.get('old_value'))} "
                         f"to {convert_to_str(diff.get('new_value'))}")

        elif status == 'removed':
            lines.append(f"Property '{'.'.join(path)}' was removed")

        list(map(lambda item: walk(item, path), diff.get('nested', [])))

    for element in diff_input:
        walk(element, ())

    return '\n'.join(lines)
