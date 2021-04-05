import numpy as np

INF = 10000


def simplex(table_description, render_info=False):
    table = table_description.table
    basic = table_description.basic
    opt = table_description.opt

    if opt == "min":
        table[-1] = -table[-1]
        table[-1][0] = -table[-1][0]

    while True:
        b = table[:-1, 0]

        new_basic_element = np.argmax(table[-1][1:]) + 1

        borders = list(table[:-1, new_basic_element])
        for i in range(len(borders)):
            if borders[i] <= 0:
                borders[i] = INF
            else:
                borders[i] = b[i] / borders[i]
        # todo: choose old != new
        old_basic_element = np.argmin(borders)

        if render_info:
            print(basic)
            print('%d --> %d' % (basic[old_basic_element], new_basic_element))
            print(table)
            print()

        if table[-1][new_basic_element] <= 0:
            break

        table[old_basic_element] = table[old_basic_element] / table[old_basic_element][new_basic_element]
        for line in range(len(table)):
            if line == old_basic_element:
                continue

            table[line] = table[line] - table[line][new_basic_element] * table[old_basic_element]

        basic[old_basic_element] = new_basic_element

    # todo: return `x` too
    if opt == "max":
        return -table[-1][0]
    else:
        return table[-1][0]
