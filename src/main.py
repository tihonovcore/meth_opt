import simplex

from tables.tables import all_basics, all_tables

for table, basic in zip(all_tables, all_basics):
    print(simplex.simplex(table, basic))
