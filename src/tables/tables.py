from tables.create_table import TableDescription

all_tables_descriptions = [
    TableDescription(
        constraints=[
            [1, 0, "<=", 40],
            [0, 1, "<=", 30],
            [1, 1, "<=", 60],
            [1, 2, "<=", 80],
        ],
        function=[2, 3],
        opt="max",
        description="from book"
    ),
    TableDescription(
        constraints=[
            [2, -1, "<=", 4],
            [1, -2, "<=", 2],
            [1, 1, "<=", 5],
        ],
        function=[3, -1],
        opt="max",
        description="from lecture"
    ),
    # Table(
    #     [
    #         [3, 1, -1, 1, "==", 4],
    #         [5, 1, 1, -1, "==", 4],
    #     ],
    #     function=[-6, -1, -4, 5],
    #     opt="min",
    #     description="from lab 4.1"
    # ),
    # start_basic: [1, 4]
    TableDescription(
        constraints=[
            [1, 3, 3,  1, "<=", 3],
            [2, 0, 3, -4, "<=", 4]
        ],
        function=[-1, 5, 1, -1],
        opt="min",
        description="from lab 4.6"
    )
]
