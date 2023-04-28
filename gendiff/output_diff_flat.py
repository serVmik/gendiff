def create_line(key, action, dct1, dct2):
    if action == 'equal':
        return f'    {key}: {dct1[key]}'

    elif action == 'changed':
        return f'  - {key}: {dct1[key]}\n  + {key}: {dct2[key]}'

    elif action == 'removed':
        return f'  - {key}: {dct1[key]}'

    else:
        return f'  + {key}: {dct2[key]}'


def create_a_string_of_diff(dct1, dct2, lst_of_diff):
    lst_of_lines = ['{']

    for diff in lst_of_diff:
        key, action = diff[0], diff[1]
        lst_of_lines.append(create_line(key, action, dct1, dct2))

    lst_of_lines.append('}')

    return '\n'.join(lst_of_lines)
