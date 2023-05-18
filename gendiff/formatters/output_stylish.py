def get_value(node, key):
    return node.get(key) if isinstance(node, dict) else node


def convert_to_string(value):
    return str(value). \
        replace('True', 'true'). \
        replace('False', 'false'). \
        replace('None', 'null')


def get_value_for_add(dct1, dct2, lst_dcts_of_diff, depth_of_dct):
    key = lst_dcts_of_diff.get('property')
    value_for_add = get_value(dct1, key)
    nesting = lst_dcts_of_diff.get('nested')

    if isinstance(value_for_add, dict):
        return create_output_stylish(
            dct1.get(key, {}), dct2.get(key, {}),
            nesting, depth_of_dct + 1
        )
    else:
        return convert_to_string(value_for_add)


def create_line(dct1, dct2, lst_dcts_of_diff, depth_of_dct):
    key = lst_dcts_of_diff.get('property')
    marker = lst_dcts_of_diff.get('marker')
    value1 = get_value_for_add(dct1, dct2, lst_dcts_of_diff, depth_of_dct)
    value2 = get_value_for_add(dct2, dct1, lst_dcts_of_diff, depth_of_dct)
    result_indent = f"{'  '}{'    ' * depth_of_dct}"

    if marker == 'changed':
        return f'{result_indent}- {key}: {value1}\n' \
               f'{result_indent}+ {key}: {value2}'

    elif marker == 'equal' or marker == 'without_marker':
        return f'{result_indent}  {key}: {value1}'

    elif marker == 'removed':
        return f'{result_indent}- {key}: {value1}'

    else:
        # marker == 'added':
        return f'{result_indent}+ {key}: {value2}'


def create_output_stylish(dct1, dct2, lst_dcts_of_diff, depth_of_dct=0):
    lst_of_lines = ['{']

    for element in lst_dcts_of_diff:
        lst_of_lines.append(
            create_line(dct1, dct2, element, depth_of_dct)
        )

    lst_of_lines.append(f"{'    ' * depth_of_dct}" + '}')
    return '\n'.join(lst_of_lines)
