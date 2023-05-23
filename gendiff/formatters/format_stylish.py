def get_value_for_add(value, depth):
    if isinstance(value, dict) or isinstance(value, list):
        return display_in_format_stylish(value, depth + 1)
    else:
        return str(value). \
            replace('True', 'true'). \
            replace('False', 'false'). \
            replace('None', 'null')


def create_line(differences, depth):
    key = differences.get('property')
    marker = differences.get('marker')
    indent = f"{'  '}{'    ' * depth}"

    if marker == 'updated':
        value1 = get_value_for_add(differences.get('value'), depth)
        value2 = get_value_for_add(differences.get('new_value'), depth)
        line = f"{indent}- {key}: {value1}\n" \
               f"{indent}+ {key}: {value2}"

    elif marker == 'equal':
        value = get_value_for_add(differences.get('value'), depth)
        line = f"{indent}  {key}: {value}"

    elif marker == 'without_marker':
        value = get_value_for_add(differences.get('nested'), depth)
        line = f"{indent}  {key}: {value}"

    elif marker == 'removed':
        value = get_value_for_add(differences.get('value'), depth)
        line = f"{indent}- {key}: {value}"

    else:
        # marker == 'added':
        value = get_value_for_add(differences.get('new_value'), depth)
        line = f"{indent}+ {key}: {value}"

    return line


def display_in_format_stylish(differences, depth=0):
    lines = ['{']

    for element in differences:
        if isinstance(element, dict):
            lines.append(create_line(element, depth))
        else:
            lines.append(create_line(
                {
                    'property': element,
                    'value': differences.get(element),
                    'marker': 'equal'
                },
                depth
            ))

    lines.append(f"{'    ' * depth}" + '}')
    return '\n'.join(lines)
