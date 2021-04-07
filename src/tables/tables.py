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
            [1,  1, "<=", 5],
        ],
        function=[3, -1],
        opt="max",
        description="from lecture"
    ),
    TableDescription(
        [
            [ 2, -1, 1, 0, "==", 1],
            [-1,  2, 0, 1, "==", 1],
        ],
        function=[1, 1, -2, -3],
        opt="min",
        description="from lab 3.8"
    ),
    TableDescription(
        [
            [3, 1, -1, 1, "==", 4],
            [5, 1, 1, -1, "==", 4],
        ],
        function=[-6, -1, -4, 5],
        opt="min",
        description="from lab 4.1"
    ),
    TableDescription(
        [
            [1, -3, -1, -2, "==", -4],
            [1, -1,  1,  0, "==",  0],
        ],
        function=[-1, -2, -3, 1],
        opt="min",
        description="from lab 4.2"
    ),
    TableDescription(
        [
            [1, 1, 0, 2, 1, "==", 5],
            [1, 1, 1, 3, 2, "==", 9],
            [0, 1, 1, 2, 1, "==", 6],
        ],
        function=[-1, -2, -1, 3, -1],
        opt="min",
        description="from lab 4.3"
    ),
    TableDescription(
        [
            [1,  1,  2, 0,  0, "==",  4],
            [0, -2, -2, 1, -1, "==", -6],
            [1, -1,  6, 1,  1, "==", 12],
        ],
        function=[-1, -1, -1, 1, -1],
        opt="min",
        description="from lab 4.4"
    ),
    TableDescription(
        [
            [1,  1, -1,  10, "==",  0],
            [1, 14, 10, -10, "==", 11],
        ],
        function=[-1, 4, -3, 10],
        opt="min",
        description="from lab 4.5"
    ),
    TableDescription(
        constraints=[
            [1, 3, 3,  1, "<=", 3],
            [2, 0, 3, -4, "<=", 4]
        ],
        function=[-1, 5, 1, -1],
        opt="min",
        description="from lab 4.6"
    ),
    TableDescription(
        constraints=[
            [3,  1, 1, 1, -2, "==", 10],
            [6,  1, 2, 3, -4, "==", 20],
            [10, 1, 3, 6, -7, "==", 30]
        ],
        function=[-1, -1, 1, -1, 2],
        opt="min",
        description="from lab 4.7"
    )
]
