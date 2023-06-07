INITIAL_DEPTH = 0
STEP_OF_DEPTH = 1
INDENT = '  '
INDENT_IN_DEPTH = '    '


def get_value_for_add(value, depth):
    if isinstance(value, dict) or isinstance(value, list):
        return create_format(value, depth + STEP_OF_DEPTH)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def create_line(diff, depth):
    key = diff.get('property')
    status = diff.get('status')
    indent = f"{INDENT}{INDENT_IN_DEPTH * depth}"

    if status == 'equal':
        old_value = get_value_for_add(diff.get('old_value'), depth)
        return f"{indent}  {key}: {old_value}"
    elif status == 'updated':
        old_value = get_value_for_add(diff.get('old_value'), depth)
        new_value = get_value_for_add(diff.get('new_value'), depth)
        return f"{indent}- {key}: {old_value}\n" \
               f"{indent}+ {key}: {new_value}"
    elif status == 'nested':
        nested_value = get_value_for_add(diff.get('nested'), depth)
        return f"{indent}  {key}: {nested_value}"
    elif status == 'removed':
        old_value = get_value_for_add(diff.get('old_value'), depth)
        return f"{indent}- {key}: {old_value}"
    elif status == 'added':
        new_value = get_value_for_add(diff.get('new_value'), depth)
        return f"{indent}+ {key}: {new_value}"


def create_format(diff, depth):
    lines = ['{']

    for property_ in diff:
        if isinstance(property_, dict):
            lines.append(create_line(property_, depth))
        else:
            lines.append(create_line(
                {
                    'property': property_,
                    'old_value': diff.get(property_),
                    'status': 'equal'
                },
                depth
            ))

    lines.append(f"{INDENT_IN_DEPTH * depth}" + '}')
    return '\n'.join(lines)


def format_stylish(diff):
    return create_format(diff, INITIAL_DEPTH)
