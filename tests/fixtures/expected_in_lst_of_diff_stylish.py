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

# equal, changed, removed, added
