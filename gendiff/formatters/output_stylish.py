from gendiff.gendiff_tools import convert_to_string, get_value

INDENT = '  '
INDENT_IN_DEPTH = '    '
STEP_OF_DEPTH = 1


def get_value_for_add(dct1, dct2, lst_dcts_of_diff, depth_of_dct):
    key = lst_dcts_of_diff.get('property')
    value_for_add = get_value(dct1, key)
    nesting = lst_dcts_of_diff.get('nested')

    if isinstance(value_for_add, dict):
        return create_output_stylish(
            dct1.get(key, {}), dct2.get(key, {}),
            nesting, depth_of_dct + STEP_OF_DEPTH
        )
    else:
        return convert_to_string(value_for_add)


def make_line(value1, value2, lst_dcts_of_diff, result_indent):
    key = lst_dcts_of_diff.get('property')
    marker = lst_dcts_of_diff.get('marker')
    space_after_key_1 = '' if not value1 else ' '
    space_after_key_2 = '' if not value2 else ' '

    if marker == 'changed':
        return f'{result_indent}- {key}:{space_after_key_1}{value1}\n' \
               f'{result_indent}+ {key}:{space_after_key_2}{value2}'

    elif marker == 'equal' or marker == 'without_marker':
        return f'{result_indent}  {key}:{space_after_key_1}{value1}'

    elif marker == 'removed':
        return f'{result_indent}- {key}:{space_after_key_1}{value1}'

    else:
        # marker == 'added':
        return f'{result_indent}+ {key}:{space_after_key_2}{value2}'


def create_line(dct1, dct2, lst_dcts_of_diff, depth_of_dct):
    value1 = get_value_for_add(dct1, dct2, lst_dcts_of_diff, depth_of_dct)
    value2 = get_value_for_add(dct2, dct1, lst_dcts_of_diff, depth_of_dct)
    result_indent = f'{INDENT}{INDENT_IN_DEPTH * depth_of_dct}'

    return make_line(value1, value2, lst_dcts_of_diff, result_indent)


def create_output_stylish(dct1, dct2, lst_dcts_of_diff, depth_of_dct=0):
    lst_of_lines = ['{']

    for element in lst_dcts_of_diff:
        lst_of_lines.append(
            create_line(dct1, dct2, element, depth_of_dct)
        )

    lst_of_lines.append(f'{INDENT_IN_DEPTH * depth_of_dct}' + '}')
    return '\n'.join(lst_of_lines)
