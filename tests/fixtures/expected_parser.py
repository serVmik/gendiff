lst_dcts_of_diff = [
    {'property': 'common',
     'marker': 'without_marker',
     'nested': [
         {'property': 'follow', 'marker': 'added'},
         {'property': 'setting1', 'marker': 'equal'},
         {'property': 'setting2', 'marker': 'removed'},
         {'property': 'setting3', 'marker': 'changed'},
         {'property': 'setting4', 'marker': 'added'},
         {'property': 'setting5', 'marker': 'added', 'nested': [
              {'property': 'key5', 'marker': 'equal'}
          ]},
         {'property': 'setting6', 'marker': 'without_marker', 'nested': [
              {'property': 'doge', 'marker': 'without_marker', 'nested': [
                   {'property': 'wow', 'marker': 'changed'}
               ]},
              {'property': 'key', 'marker': 'equal'},
              {'property': 'ops', 'marker': 'added'}
          ]}
     ]},
    {'property': 'group1', 'marker': 'without_marker', 'nested': [
         {'property': 'baz', 'marker': 'changed'},
         {'property': 'foo', 'marker': 'equal'},
         {'property': 'nest', 'marker': 'changed', 'nested': [
              {'property': 'key', 'marker': 'equal'}
          ]}
     ]},
    {'property': 'group2', 'marker': 'removed', 'nested': [
         {'property': 'abc', 'marker': 'equal'},
         {'property': 'deep', 'marker': 'equal', 'nested': [
              {'property': 'id', 'marker': 'equal'}
          ]}
     ]},
    {'property': 'group3', 'marker': 'added', 'nested': [
         {'property': 'deep', 'marker': 'equal', 'nested': [
              {'property': 'id', 'marker': 'equal', 'nested': [
                   {'property': 'number', 'marker': 'equal'}
               ]}
          ]},
         {'property': 'fee', 'marker': 'equal'}
     ]}
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
