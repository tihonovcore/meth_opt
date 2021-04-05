import simplex

from tables.tables import all_basics, all_tables

for table, basic, opt in zip(all_tables, all_basics, ["max", "max", "min", "min"]):
    print()
    print(table[-1][1:])
    print(simplex.simplex(table, basic, opt))
