def create_updated(old_value, new_value):
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return {
            'status': 'nested',
            'nested': create_diff(old_value, new_value)
        }
    else:
        return {
            'status': 'updated',
            'old_value': old_value,
            'new_value': new_value
        }


def create_changes(old_dict, new_dict, key):
    old_value = old_dict.get(key)
    new_value = new_dict.get(key)

    if old_value == new_value:
        changes = {
            'status': 'equal',
            'old_value': old_value
        }

    elif key in old_dict and key in new_dict:
        changes = create_updated(old_value, new_value)

    elif key in old_dict:
        changes = {
            'status': 'removed',
            'old_value': old_value
        }

    else:
        # key in dict2:
        changes = {
            'status': 'added',
            'new_value': new_value
        }

    return changes


def create_diff(old_dict, new_dict):
    keys = sorted(list(set(old_dict.keys()).union(new_dict.keys())))
    diff = []

    for key in keys:
        property_ = {'property': key}
        property_.update(create_changes(old_dict, new_dict, key))
        diff.append(property_)

    return diff
