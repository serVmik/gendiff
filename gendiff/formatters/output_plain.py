# result_line = f"Property {path} was {action}{old_value}{new_value}"
from gendiff.gendiff_tools import get_value_from_dct_using_path


def create_output_plain(dct1, dct2, lst_of_diff):
    def walk(value1, value2, node, path):
        path += (node.get('property'),)
        action = node.get('marker')

        if 'nested' not in node and action == 'added':
            value = get_value_from_dct_using_path(dct2, path)
            print(f"Property '{'.'.join(path)}' was {value}")

        lst_of_nested_property = node.get('nested', ())
        list(map(
            lambda item: walk(dct1, dct2, item, path),
            lst_of_nested_property
        ))

    for element in lst_of_diff:
        walk(dct1, dct2, element, ())
