def has_node_another_node(node):
    return not isinstance(node[0], list) and isinstance(node[-1], list)


def get_value_from_dct(dct, key):
    return dct.get(key) if isinstance(dct, dict) else dct


def get_value_from_dct_1(dct1, dct2, key):
    if isinstance(dct1, dict) and key in dct1:
        return get_value_from_dct(dct1, key)
    elif isinstance(dct2, dict) and key in dct2:
        return get_value_from_dct(dct2, key)


def create_text_to_print_in_one_string(dct1_in, dct2_in, lst_of_diff):
    INDENT = '  '
    INDENT_IN_DEPTH = '    '
    DEPTH_START_WITH = 0
    STEP_OF_DEPTH = 1

    def create_line(dct1, dct2, element, depth):
        indent = f'{INDENT}{INDENT_IN_DEPTH * depth}'
        key, action = element[0], element[1]
        value1 = get_value_from_dct(dct1, key)
        value2 = get_value_from_dct(dct2, key)
        value = get_value_from_dct_1(dct1, dct2, key)
        print(f'key ={key} // value = {value}')

        if action == 'equal':
            if has_node_another_node(element):
                value1 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            if has_node_another_node(element):
                value2 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            return f'{indent}  {key}: {value2}'
        elif action == 'changed':
            if has_node_another_node(element):
                value1 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            if has_node_another_node(element):
                value2 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            return f'{indent}- {key}: {value1}\n{indent}+ {key}: {value2}'
        elif action == 'removed':
            if has_node_another_node(element):
                value1 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            if has_node_another_node(element):
                value2 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            return f'{indent}- {key}: {value1}'
        else:
            # action == 'added':
            if has_node_another_node(element):
                value2 = create_line_to_add(
                    value1, value2, element[-1], depth + STEP_OF_DEPTH
                )
            return f'{indent}+ {key}: {value2}'

    def create_line_to_add(dct1, dct2, node, depth):
        lst_of_lines = ['{']

        if isinstance(node, list) and not isinstance(node[-1], list):
            return lst_of_lines.append(create_line(dct1, dct2, node, depth))

        for element in node:
            lst_of_lines.append(
                create_line(dct1, dct2, element, depth)
            )

        lst_of_lines.append(f'{INDENT_IN_DEPTH * depth}' + '}')
        return '\n'.join(lst_of_lines)

    result_string = create_line_to_add(
        dct1_in, dct2_in, lst_of_diff, DEPTH_START_WITH
    )
    return result_string
