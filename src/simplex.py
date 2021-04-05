import numpy as np

INF = 10000


def simplex(table, basic, render_info=False):
    stat = set()
    # while True:
    for _ in range(10):
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

    return table[-1][0]