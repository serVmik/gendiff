def create_a_string_of_diff(dct1, dct2, lst_of_actions_for_dct_key):
    result_strings = '{\n'
    for action_for_dct_key in lst_of_actions_for_dct_key:
        key = action_for_dct_key[0]
        action = action_for_dct_key[1]
        if action == 'equal':
            result_strings += f'    {key}: {dct1[key]}\n'
        elif action == 'changed':
            result_strings += f'  - {key}: {dct1[key]}\n'\
                            + f'  + {key}: {dct2[key]}\n'
        elif action == 'removed':
            result_strings += f'  - {key}: {dct1[key]}\n'
        else:       # action == 'added'
            result_strings += f'  + {key}: {dct2[key]}\n'
    result_strings += '}'

    return result_strings
