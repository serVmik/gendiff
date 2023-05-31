differences = [
    {
        "property": "common",
        "status": "nested",
        "nested": [
            {
                "property": "follow",
                "status": "added",
                "new_value": "false"
            },
            {
                "property": "setting1",
                "status": "equal",
                "value": "Value 1"
            },
            {
                "property": "setting2",
                "status": "removed",
                "value": 200
            },
            {
                "property": "setting3",
                "status": "updated",
                "value": "true",
                "new_value": "null"
            },
            {
                "property": "setting4",
                "status": "added",
                "new_value": "blah blah"
            },
            {
                "property": "setting5",
                "status": "added",
                "new_value": {
                    "key5": "value5"
                }
            },
            {
                "property": "setting6",
                "status": "nested",
                "nested": [
                    {
                        "property": "doge",
                        "status": "nested",
                        "nested": [
                            {
                                "property": "wow",
                                "status": "updated",
                                "value": "",
                                "new_value": "so much"
                            }
                        ]
                    },
                    {
                        "property": "key",
                        "status": "equal",
                        "value": "value"
                    },
                    {
                        "property": "ops",
                        "status": "added",
                        "new_value": "vops"
                    }
                ]
            }
        ]
    },
    {
        "property": "group1",
        "status": "nested",
        "nested": [
            {
                "property": "baz",
                "status": "updated",
                "value": "bas",
                "new_value": "bars"
            },
            {
                "property": "foo",
                "status": "equal",
                "value": "bar"
            },
            {
                "property": "nest",
                "status": "updated",
                "value": {
                    "key": "value"
                },
                "new_value": "str"
            }
        ]
    },
    {
        "property": "group2",
        "status": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "property": "group3",
        "status": "added",
        "new_value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]

dct1 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": "true",
        "setting6": {
            "key": "value",
            "doge": {
                "wow": ""
            }
        }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45
        }
    }
}

dct2 = {
    "common": {
        "follow": "false",
        "setting1": "Value 1",
        "setting3": "null",
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much"
            }
        }
    },
    "group1": {
        "foo": "bar",
        "baz": "bars",
        "nest": "str"
    },
    "group3": {
        "deep": {
            "id": {
                "number": 45
            }
        },
        "fee": 100500
    }
}
