from gendiff.gendiff_tools import convert_to_string

INDENT = '  '
INDENT_IN_DEPTH = '    '
STEP_OF_DEPTH = 1
VALUE_IF_KEY_NOT_IN_DICT = {}


def create_line(dct1, dct2, node, depth_of_dct):
    indent = f'{INDENT}{INDENT_IN_DEPTH * depth_of_dct}'
    key, action = node[0], node[1]

    def get_value_for_add(dct):
        value_for_add = dct.get(key)

        if isinstance(value_for_add, dict):
            return make_lines(
                dct1.get(key, VALUE_IF_KEY_NOT_IN_DICT),
                dct2.get(key, VALUE_IF_KEY_NOT_IN_DICT),
                node[-1], depth_of_dct + STEP_OF_DEPTH
            )
        else:
            return convert_to_string(value_for_add)

    def get_value_for_create_line(value_for_create_line):
        if value_for_create_line == 0:
            if key in dct1:
                return get_value_for_create_line(value_for_create_line=1)
            else:
                return get_value_for_create_line(value_for_create_line=2)

        elif value_for_create_line == 1:
            return get_value_for_add(dct1)
        else:
            return get_value_for_add(dct2)

    value = get_value_for_create_line(value_for_create_line=0)

    if action == 'changed':
        value1 = get_value_for_create_line(value_for_create_line=1)
        value2 = get_value_for_create_line(value_for_create_line=2)

        return f'{indent}- {key}: {value1}\n' \
               f'{indent}+ {key}: {value2}'

    elif action == 'equal':
        return f'{indent}  {key}: {value}'

    elif action == 'removed':
        return f'{indent}- {key}: {value}'

    else:
        # action == 'added':
        return f'{indent}+ {key}: {value}'


def make_lines(dct1, dct2, lst_of_diff, depth_of_dct=0):
    lst_of_lines = ['{']

    for element in lst_of_diff:
        lst_of_lines.append(
            create_line(dct1, dct2, element, depth_of_dct)
        )

    lst_of_lines.append(f'{INDENT_IN_DEPTH * depth_of_dct}' + '}')
    return '\n'.join(lst_of_lines)
