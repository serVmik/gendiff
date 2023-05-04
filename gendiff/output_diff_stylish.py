INDENT = '  '
INDENT_IN_DEPTH = '    '
DEPTH_START_WITH = 0
STEP_OF_DEPTH = 1


def is_node(node):
    return not isinstance(node[0], list) and isinstance(node[-1], list)


def create_text_to_print_in_one_string(dct1_in, dct2_in, lst_of_diff):
    def create_line(dct1, dct2, node, depth):
        indent = f'{INDENT}{INDENT_IN_DEPTH * depth}'
        key, action = node[0], node[1]
        print(f"key = {key}")

        if action == 'equal':
            if is_node(node):
                value1 = create_line_to_add(
                    dct1.get(key), dct2.get(key),
                    node[-1], depth + STEP_OF_DEPTH
                )
            else:
                value1 = dct1.get(key)
            return f'{indent}  {key}: {value1}'
        elif action == 'changed':
            return f'{indent}- {key}: {dct1}\n' \
                   f'{indent}+ {key}: {dct2}'
        elif action == 'removed':
            return f'{indent}- {key}: {dct1}'
        else:
            # action == 'added':
            return f'{indent}+ {key}: {dct2}'

    def create_line_to_add(dct1, dct2, node, depth):
        lst_of_lines = ['{']

        for element in node:

            lst_of_lines.append(
                create_line(dct1, dct2, element, depth)
            )

        lst_of_lines.append(f'{INDENT_IN_DEPTH * depth}' + '}')
        return '\n'.join(lst_of_lines)

    print(f"lst_of_diff = {lst_of_diff}")
    result_string = create_line_to_add(
        dct1_in, dct2_in, lst_of_diff, DEPTH_START_WITH
    )
    return result_string
