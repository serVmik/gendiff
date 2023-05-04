from gendiff.gendiff_tools import convert_to_string

INDENT = '  '
INDENT_IN_DEPTH = '    '
STEP_OF_DEPTH = 1
VALUE_IF_KEY_NOT_IN_DICT = {}


def is_node_parent(node):
    return not isinstance(node[0], list) and isinstance(node[-1], list)


def get_value_from_dct(dct1, dct2, node, depth_of_dct):
    key = node[0]

    if is_node_parent(node):
        return make_lines(
            dct1.get(key, VALUE_IF_KEY_NOT_IN_DICT),
            dct2.get(key, VALUE_IF_KEY_NOT_IN_DICT),
            node[-1], depth_of_dct + STEP_OF_DEPTH
        )
    elif key in dct1:
        return convert_to_string(dct1.get(key))
    else:
        # key in dct2:
        return convert_to_string(dct2.get(key))


def create_line(dct1, dct2, node, depth_of_dct):
    indent = f'{INDENT}{INDENT_IN_DEPTH * depth_of_dct}'
    key, action = node[0], node[1]

    value1 = get_value_from_dct(dct1, dct2, node, depth_of_dct)
    value2 = get_value_from_dct(dct2, dct1, node, depth_of_dct)

    if action == 'equal':
        return f'{indent}  {key}: {value1}'
    elif action == 'changed':
        return f'{indent}- {key}: {value1}\n' \
               f'{indent}+ {key}: {value2}'
    elif action == 'removed':
        return f'{indent}- {key}: {value1}'
    else:
        # action == 'added':
        return f'{indent}+ {key}: {value2}'


def make_lines(dct1, dct2, node, depth_of_dct=0):
    lst_of_lines = ['{']

    for element in node:
        lst_of_lines.append(
            create_line(dct1, dct2, element, depth_of_dct)
        )

    lst_of_lines.append(f'{INDENT_IN_DEPTH * depth_of_dct}' + '}')
    return '\n'.join(lst_of_lines)
