def create_line(lst_of_lines, indent, key, action, dct1, dct2):
    if action == 'equal':
        lst_of_lines.append(f'{indent}  {key}: {dct1[key]}')

    elif action == 'changed':
        lst_of_lines.append(f'{indent}- {key}: {dct1[key]}')
        lst_of_lines.append(f'{indent}+ {key}: {dct2[key]}')

    elif action == 'removed':
        lst_of_lines.append(f'{indent}- {key}: {dct1[key]}')

    else:
        # action == 'added':
        lst_of_lines.append(f'{indent}+ {key}: {dct2[key]}')

    return lst_of_lines


def create_a_string_of_diff(dct1, dct2, lst_of_diff):
    INDENT = '  '
    INDENT_IN_DEPTH = '  '
    DEPTH_START_WITH = 0

    def join_lines_of_diff(depth):
        lst_of_lines = ['{']
        indent = f'{INDENT}{INDENT_IN_DEPTH * depth}'

        for diff in lst_of_diff:
            key, action = diff[0], diff[1]

            if len(key) > 2:
                make_lines(key, depth + 1)

            lst_of_lines = create_line(
                lst_of_lines, indent, key, action, dct1, dct2
            )

        lst_of_lines.append('}')

        result_string = '\n'.join(lst_of_lines)
        return result_string

    def make_lines(value_for_get_lines, depth):
        if isinstance(value_for_get_lines, dict):
            return join_lines_of_diff(depth + 1)
        else:
            return str(value_for_get_lines)

    return make_lines({}, DEPTH_START_WITH)
