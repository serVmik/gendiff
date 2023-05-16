from gendiff.gendiff_tools import convert_to_string

INDENT = '  '
INDENT_IN_DEPTH = '    '
STEP_OF_DEPTH = 1


def create_line(dct1, dct2, lst_dcts_of_diff, depth_of_dct):
    key = lst_dcts_of_diff.get('property')
    marker = lst_dcts_of_diff.get('marker')
    indent = f'{INDENT}{INDENT_IN_DEPTH * depth_of_dct}'
    space_after_key_1 = space_after_key_2 = ' '

    value1 = convert_to_string(dct1.get(key))
    value2 = convert_to_string(dct2.get(key))

    if marker == 'added':
        return f'{indent}+ {key}:{space_after_key_2}{value2}'

    elif marker == 'removed':
        return f'{indent}- {key}:{space_after_key_1}{value1}'

    elif marker == 'equal' or marker == 'without_marker':
        return f'{indent}  {key}:{space_after_key_1}{value1}'

    else:
        return f'{indent}- {key}:{space_after_key_1}{value1}\n' \
               f'{indent}+ {key}:{space_after_key_2}{value2}'


def create_output_stylish(dct1, dct2, lst_dcts_of_diff, depth_of_dct=0):
    lst_of_lines = ['{']

    for element in lst_dcts_of_diff:
        lst_of_lines.append(
            create_line(dct1, dct2, element, depth_of_dct)
        )

    lst_of_lines.append(f'{INDENT_IN_DEPTH * depth_of_dct}' + '}')
    return '\n'.join(lst_of_lines)
