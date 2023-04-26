def create_a_string_of_diff(dct1, dct2, lst_of_diff):
    default_indent = '  '
    default_depth = 0

    def join_lines_of_deff(lst_of_diff, indent, depth):
        lst_of_lines = ['{\n']

        for diff in lst_of_diff:
            key, action = diff[0], diff[1]

            if action == 'equal':
                lst_of_lines.append(
                    f'{indent}{indent * depth}  {key}: {dct1[key]}\n')

            elif action == 'changed':
                lst_of_lines.append(
                    f'{indent}{indent * depth}- {key}: {dct1[key]}\n')

                lst_of_lines.append(
                    f'{indent}{indent * depth}+ {key}: {dct2[key]}\n')

            elif action == 'removed':
                lst_of_lines.append(
                    f'{indent}{indent * depth}- {key}: {dct1[key]}\n')

            elif action == 'added':
                lst_of_lines.append(
                    f'{indent}{indent * depth}+ {key}: {dct2[key]}\n')

        lst_of_lines.append('}')

        result_string = ''.join(lst_of_lines)
        return result_string

    def make_lines(value_for_get_lines, default_indent, default_depth):
        if isinstance(value_for_get_lines, dict):
            return join_lines_of_deff(
                lst_of_diff, default_indent, default_depth
                )
        else:
            return str(value_for_get_lines)

    return make_lines(default_indent, default_depth)
