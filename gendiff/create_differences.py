def make_if_updated(value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        return {
            'marker': 'without_marker',
            'nested': create_differences(value1, value2)
        }
    else:
        return {
            'marker': 'updated',
            'value': value1,
            'new_value': value2
        }


def create_changes(dict1, dict2, key):
    value1 = dict1.get(key)
    value2 = dict2.get(key)

    if value1 == value2:
        changes = {
            'marker': 'equal',
            'value': value1
        }

    elif key in dict1 and key in dict2:
        changes = make_if_updated(value1, value2)

    elif key in dict1:
        changes = {
            'marker': 'removed',
            'value': value1
        }

    else:
        # key in dict2:
        changes = {
            'marker': 'added',
            'new_value': value2
        }

    return changes


def create_differences(dict1, dict2):
    keys = sorted(list(set(dict1.keys()).union(dict2.keys())))
    differences = list(map(lambda key: {'property': key}, keys))

    for property_ in differences:
        key_ = property_.get('property')
        property_.update(create_changes(dict1, dict2, key_))

    return differences
