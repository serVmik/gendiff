def create_a_string_of_diff(dct1, dct2, lst_of_diff):
    lst_of_diff_string = ['{\n']

    for diff in lst_of_diff:
        key, action = diff[0], diff[1]
        nesting_level = len(diff[0])

        indent = f'{"    " * nesting_level}'
        
        if action == 'equal':
            lst_of_diff_string.append(f'{indent}  {key}: {dct1[key]}\n')

        elif action == 'changed':
            lst_of_diff_string.append(f'{indent}- {key}: {dct1[key]}\n')
            lst_of_diff_string.append(f'{indent}+ {key}: {dct2[key]}\n')

        elif action == 'removed':
            lst_of_diff_string.append(f'{indent}- {key}: {dct1[key]}\n')

        elif action == 'added':
            lst_of_diff_string.append(f'{indent}+ {key}: {dct2[key]}\n')

    lst_of_diff_string.append('}')
    result_string = ''.join(lst_of_diff_string)

    return result_string
