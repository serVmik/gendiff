def create_a_string_of_diff(dct1, dct2, key):
    if dct1.get(key) == dct2.get(key):
        return f'    {key}: {dct1[key]}\n'
    elif key in dct1 and key in dct2:
        return f'  - {key}: {dct1[key]}\n  + {key}: {dct2[key]}\n'
    elif key in dct1:
        return f'  - {key}: {dct1[key]}\n'
    else:
        return f'  + {key}: {dct2[key]}\n'
