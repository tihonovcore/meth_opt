from tables.create_table import create_table

table_from_book, basic_from_book = create_table(
    constraints=[
        [1, 0, "<=", 40],
        [0, 1, "<=", 30],
        [1, 1, "<=", 60],
        [1, 2, "<=", 80],
    ],
    function=[2, 3]
)

table_from_lecture, basic_from_lecture = create_table(
    [
     [2, -1, "<=", 4],
     [1, -2, "<=", 2],
     [1,  1, "<=", 5],
    ],
    function=[3, -1]
)

table_from_lab_4_1, _ = create_table(
    [
     [3,  1, -1,  1, "==", 4],
     [5,  1,  1, -1, "==", 4],
    ],
    function=[-6, -1, -4, 5]
)
basic_from_lab_4_1 = [1, 4]

table_from_lab_4_6, basic_from_lab_4_6 = create_table(
    constraints=[
        [1, 3, 3,  1, "<=", 3],
        [2, 0, 3, -4, "<=", 4]
    ],
    function=[-1, 5, 1, -1]
)

all_tables = [table_from_book, table_from_lecture, table_from_lab_4_1, table_from_lab_4_6]
all_basics = [basic_from_book, basic_from_lecture, basic_from_lab_4_1, basic_from_lab_4_6]
