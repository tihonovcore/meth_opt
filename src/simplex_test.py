import numpy as np

import simplex

from tables.create_table import create_simplex_table
from tables.tables import all_tables_descriptions


def eq(left, right):
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]

    diff = np.array(left) - right
    return diff @ diff < 1e-5


def find_table_by_description(description):
    for d in all_tables_descriptions:
        if d.description == description:
            return d

    return None


def common_simplex_test(description):
    print(description, end='')

    table_description = find_table_by_description(description)
    create_simplex_table(table_description)
    return simplex.simplex(table_description)


def test_from_book():
    f_opt, x_opt = common_simplex_test("from book")

    assert eq(f_opt, 140.0)
    assert eq(x_opt, [40.0, 20.0])

    print('\tOK')


def test_from_lecture():
    f_opt, x_opt = common_simplex_test("from lecture")

    assert eq(f_opt, 7.0)
    assert eq(x_opt, [3.0, 2.0])

    print('\tOK')


def test_from_lab_38():
    f_opt, x_opt = common_simplex_test("from lab 3.8")

    assert eq(f_opt, -5.0)
    assert eq(x_opt, [0, 0, 1, 1])

    print('\tOK')


def test_from_lab_41():
    f_opt, x_opt = common_simplex_test("from lab 4.1")

    assert eq(f_opt, -16.0)
    assert eq(x_opt, [0, 0, 4, 0])

    print('\tOK')


def test_from_lab_42():
    f_opt, x_opt = common_simplex_test("from lab 4.2")

    assert eq(f_opt, -6.0)
    assert eq(x_opt, [2, 2, 0, 0])

    print('\tOK')


def test_from_lab_43():
    f_opt, x_opt = common_simplex_test("from lab 4.3")

    assert eq(f_opt, -11.0)
    assert eq(x_opt, [0, 5, 1, 0, 0])

    print('\tOK')


def test_from_lab_44():
    f_opt, x_opt = common_simplex_test("from lab 4.4")

    assert eq(f_opt, -20.0)
    assert eq(x_opt, [0, 4, 0, 0, 16])

    print('\tOK')


def test_from_lab_45():
    f_opt, x_opt = common_simplex_test("from lab 4.5")

    assert eq(f_opt, -4.0)
    assert eq(x_opt, [1, 0, 1, 0])

    print('\tOK')


def test_from_lab_46():
    f_opt, x_opt = common_simplex_test("from lab 4.6")

    assert eq(f_opt, -3.0)
    assert eq(x_opt, [8.0 / 3, 0, 0, 1.0 / 3])

    print('\tOK')


def test_from_lab_47():
    f_opt, x_opt = common_simplex_test("from lab 4.7")

    assert eq(f_opt, -10.0)
    assert eq(x_opt, [0, 6, 0, 4, 0])

    print('\tOK')


if __name__ == '__main__':
    test_from_book()
    test_from_lecture()
    test_from_lab_38()
    test_from_lab_41()
    test_from_lab_42()
    test_from_lab_43()
    test_from_lab_44()
    test_from_lab_45()
    test_from_lab_46()
    test_from_lab_47()
