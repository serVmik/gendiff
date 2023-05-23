def convert_to_str(value):
    if isinstance(value, str):
        return f"'{value}'"

    elif isinstance(value, dict):
        return '[complex value]'

    return str(value).\
        replace('True', 'true').\
        replace('False', 'false').\
        replace('None', 'null')


def display_in_format_plain(differences_input):
    lines = []

    def walk(differences, path):
        path += (differences.get('property'),)
        marker = differences.get('marker')

        if marker == 'added':
            lines.append(f"Property '{'.'.join(path)}' was added with value: "
                         f"{convert_to_str(differences.get('new_value'))}")

        elif marker == 'updated':
            lines.append(f"Property '{'.'.join(path)}' was updated. "
                         f"From {convert_to_str(differences.get('value'))} "
                         f"to {convert_to_str(differences.get('new_value'))}")

        elif marker == 'removed':
            lines.append(f"Property '{'.'.join(path)}' was removed")

        list(map(lambda item: walk(item, path), differences.get('nested', [])))

    for element in differences_input:
        walk(element, ())

    return '\n'.join(lines)
