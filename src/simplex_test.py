import numpy as np

import simplex

from tables.create_table import create_simplex_table
from tables.tables import all_tables_descriptions


def eq(left, right):
    diff = np.array(left) - right
    return diff @ diff < 1e-5


def find_table_by_description(description):
    for d in all_tables_descriptions:
        if d.description == description:
            return d

    return None


def test_from_book():
    table_description = find_table_by_description("from book")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == 140.0
    assert eq(x_opt, [40.0, 20.0])


def test_from_lecture():
    table_description = find_table_by_description("from lecture")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == 7.0
    assert eq(x_opt, [3.0, 2.0])


def test_from_lab_41():
    table_description = find_table_by_description("from lab 4.1")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -16.0
    assert eq(x_opt, [0, 0, 4, 0])


def test_from_lab_42():
    table_description = find_table_by_description("from lab 4.2")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description, True)

    print((f_opt, x_opt))

    assert f_opt == -16.0
    assert eq(x_opt, [0, 0, 4, 0])


def test_from_lab_43():
    table_description = find_table_by_description("from lab 4.3")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -11.0
    assert eq(x_opt, [0, 5, 1, 0, 0])


def test_from_lab_44():
    table_description = find_table_by_description("from lab 4.4")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -20.0
    assert eq(x_opt, [0, 4, 0, 0, 16])


def test_from_lab_45():
    table_description = find_table_by_description("from lab 4.5")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -4.0
    assert eq(x_opt, [1, 0, 1, 0])


def test_from_lab_46():
    table_description = find_table_by_description("from lab 4.6")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -3.0
    assert eq(x_opt, [8.0 / 3, 0, 0, 1.0 / 3])


def test_from_lab_47():
    table_description = find_table_by_description("from lab 4.7")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -10.0
    assert eq(x_opt, [0, 6, 0, 4, 0])


if __name__ == '__main__':
    test_from_book()
    test_from_lecture()
    test_from_lab_41()
    # test_from_lab_42() # todo
    test_from_lab_43()
    test_from_lab_44()
    test_from_lab_45()
    test_from_lab_46()
    test_from_lab_47()
