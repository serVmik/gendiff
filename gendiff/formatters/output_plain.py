def is_property_nested(node):
    return node[1] == 'without_marker'


def get_depth_of_node(node_lst_of_diff, path):
    path += node_lst_of_diff[0]
    if is_property_nested(node_lst_of_diff):
        get_depth_of_node(node_lst_of_diff[2], path)
    return path


def create_line(dct1, dct2, node_lst_of_diff):
    path = node_lst_of_diff[0]

    if is_property_nested(node_lst_of_diff):
        path = get_depth_of_node(node_lst_of_diff[2], path)

    action = ''
    value = ''

    line = ['Property', f'{path}', f'{action}', f'{value}']

    return


def create_output_plain(dct1, dct2, lst_of_diff):
    lst_of_lines = ['1', '2']

    for element in lst_of_diff:
        lst_of_lines.append(
            create_line(dct1, dct2, element)
        )

    return '\n'.join(lst_of_lines)
