import json


def create_output_json(diff):
    return json.dumps(diff, indent=4)
