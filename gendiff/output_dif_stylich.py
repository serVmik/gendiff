# def create_line(indent, diff, dct1, dct2):
#     key, action = diff[0], diff[1]
#
#     if action == 'equal':
#         return f'{indent}  {key}: {dct1[key]}'
#
#     elif action == 'changed':
#         return f'{indent}- {key}: {dct1[key]}\n{indent}+ {key}: {dct2[key]}'
#
#     elif action == 'removed':
#         return f'{indent}- {key}: {dct1[key]}'
#
#     else:
#         # action == 'added':
#         return f'{indent}+ {key}: {dct2[key]}'
#
#
# def create_a_string_of_diff(dct1, dct2, lst_of_diff):
#     INDENT = '  '
#     INDENT_IN_DEPTH = '    '
#     DEPTH_START_WITH = 0
#
#     def join_lines_of_diff(depth):
#         lst_of_lines = ['{']
#         indent = f'{INDENT}{INDENT_IN_DEPTH * depth}'
#
#         for diff in lst_of_diff:
#             key, action = diff[0], diff[1]
#
#             if len(key) > 2:
#                 make_lines(key, depth + 1)
#
#             lst_of_lines.append(create_line(indent, diff, dct1, dct2))
#
#         lst_of_lines.append('}')
#
#         result_string = '\n'.join(lst_of_lines)
#         return result_string
#
#     def make_lines(value_for_get_lines, depth):
#         if isinstance(value_for_get_lines, dict):
#             return join_lines_of_diff(depth + 1)
#         else:
#             return str(value_for_get_lines)
#
#     return make_lines({}, DEPTH_START_WITH)
