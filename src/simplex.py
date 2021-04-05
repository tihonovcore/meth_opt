import numpy as np

INF = 10000

def simplex(table, basic):
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
        # old_basic_element = np.argmin(list(map(lambda t: t if t > 0 else INF, b / list(table[:-1, new_basic_element]))))

        print(basic)
        print('%d --> %d' % (basic[old_basic_element], new_basic_element))
        # print('F: %f' % table[-1][0])
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
