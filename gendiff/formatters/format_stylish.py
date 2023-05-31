INITIAL_DEPTH = 0
STEP_OF_DEPTH = 1
INDENT = '  '
INDENT_IN_DEPTH = '    '


def get_value_for_add(value, depth):
    if isinstance(value, dict) or isinstance(value, list):
        return create_format(value, depth + STEP_OF_DEPTH)

    return str(value). \
        replace('True', 'true'). \
        replace('False', 'false'). \
        replace('None', 'null')


def create_line(diff, depth):
    key = diff.get('property')
    status = diff.get('status')
    indent = f"{INDENT}{INDENT_IN_DEPTH * depth}"

    if status == 'equal':
        value = get_value_for_add(diff.get('old_value'), depth)
        line = f"{indent}  {key}: {value}"

    elif status == 'updated':
        value1 = get_value_for_add(diff.get('old_value'), depth)
        value2 = get_value_for_add(diff.get('new_value'), depth)
        line = f"{indent}- {key}: {value1}\n" \
               f"{indent}+ {key}: {value2}"

    elif status == 'nested':
        value = get_value_for_add(diff.get('nested'), depth)
        line = f"{indent}  {key}: {value}"

    elif status == 'removed':
        value = get_value_for_add(diff.get('old_value'), depth)
        line = f"{indent}- {key}: {value}"

    else:
        # status == 'added':
        value = get_value_for_add(diff.get('new_value'), depth)
        line = f"{indent}+ {key}: {value}"

    return line


def create_format(diff, depth):
    lines = ['{']

    for element in diff:
        if isinstance(element, dict):
            lines.append(create_line(element, depth))
        else:
            lines.append(create_line(
                {
                    'property': element,
                    'old_value': diff.get(element),
                    'status': 'equal'
                },
                depth
            ))

    lines.append(f"{INDENT_IN_DEPTH * depth}" + '}')
    return '\n'.join(lines)


def format_stylish(diff):
    return create_format(diff, INITIAL_DEPTH)
