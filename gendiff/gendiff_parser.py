def create_a_string_of_diff(dct1, dct2, lst_of_actions_for_dct_key):
    result_string_in_lst = ['{\n']

    for action_for_dct_key in lst_of_actions_for_dct_key:
        key, action = action_for_dct_key[0], action_for_dct_key[1]

        if action == 'equal':
            result_string_in_lst.append(f'    {key}: {dct1[key]}\n')

        elif action == 'changed':
            result_string_in_lst.append(f'  - {key}: {dct1[key]}\n')
            result_string_in_lst.append(f'  + {key}: {dct2[key]}\n'
)
        elif action == 'removed':
            result_string_in_lst.append(f'  - {key}: {dct1[key]}\n')

        elif action == 'added':
            result_string_in_lst.append(f'  + {key}: {dct2[key]}\n')

    result_string_in_lst.append('}')

    result_string = ''.join(result_string_in_lst)

    return result_string
