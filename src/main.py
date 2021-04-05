import simplex
from tables.create_table import create_simplex_table

from tables.tables import all_tables_descriptions

for table_description in all_tables_descriptions:
    create_simplex_table(table_description)
    print(simplex.simplex(table_description))
