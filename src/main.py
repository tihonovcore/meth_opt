import numpy as np

import simplex

from tables.tables import all_basics, all_tables

# todo: get from `create_table` or by algorithm
xs = [np.array([0, 0, 40, 30, 60, 80]), np.array([0, 0, 4, 2, 5]), np.array([0, 0, 0, 0, 4, 4])]

for table, basic, x in zip(all_tables, all_basics, xs):
    table[-1][0] = x @ table[-1][1:]
    print(simplex.simplex(table, basic))
