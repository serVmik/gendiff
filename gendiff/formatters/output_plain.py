# result_line = f"Property {path} was {action}{old_value}{new_value}"
import os


def create_lines_of_diff(lst_of_diff):
    def walk(node, path):
        path = os.path.join(path, node.get('property')).replace('/', '.')
        if 'nested' not in node:
            print(f'{path}')
            return

        lst_of_nested_property = node.get('nested')
        list(map(lambda item: walk(item, path), lst_of_nested_property))

    for element in lst_of_diff:
        walk(element, '')

    return


def create_output_plain(dct1, dct2, lst_of_diff):
    create_lines_of_diff(lst_of_diff)
