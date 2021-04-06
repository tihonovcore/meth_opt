import numpy as np

import simplex

from tables.create_table import create_simplex_table
from tables.tables import all_tables_descriptions


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
    assert x_opt == [40.0, 20.0]


def test_from_lecture():
    table_description = find_table_by_description("from lecture")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == 7.0
    assert x_opt == [3.0, 2.0]


def test_from_lab_41():
    table_description = find_table_by_description("from lab 4.1")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -16.0
    assert x_opt == [0, 0, 4, 0]


def test_from_lab_46():
    table_description = find_table_by_description("from lab 4.6")
    create_simplex_table(table_description)
    f_opt, x_opt = simplex.simplex(table_description)

    assert f_opt == -3.0
    assert x_opt == [8.0 / 3, 0, 0, 1.0 / 3]


if __name__ == '__main__':
    test_from_book()
    test_from_lecture()
    test_from_lab_41()
    test_from_lab_46()
