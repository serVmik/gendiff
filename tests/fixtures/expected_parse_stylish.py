lst_of_diff = [
    ['common', 'without_marker', [
        ['follow', 'added'],
        ['setting1', 'equal'],
        ['setting2', 'removed'],
        ['setting3', 'changed'],
        ['setting4', 'added'],
        ['setting5', 'added', [
            ['key5', 'equal']
        ]
         ],
        ['setting6', 'without_marker', [
            ['doge', 'without_marker', [
                ['wow', 'changed']
            ]
             ],
            ['key', 'equal'],
            ['ops', 'added']
        ]
         ]
    ]
     ],
    ['group1', 'without_marker', [
        ['baz', 'changed'],
        ['foo', 'equal'],
        ['nest', 'changed', [
            ['key', 'equal']
        ]
         ]
    ]
     ],
    ['group2', 'removed', [
        ['abc', 'equal'],
        ['deep', 'equal', [
            ['id', 'equal']
        ]
         ]
    ]
     ],
    ['group3', 'added', [
        ['deep', 'equal', [
            ['id', 'equal', [
                ['number', 'equal']
            ]
             ]
        ]
         ], ['fee', 'equal']
    ]
     ]
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
