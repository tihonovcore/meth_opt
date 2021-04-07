import numpy as np

INF = 10000
EPS = 1e-5


def simplex(table_description, render_info=False):
    table = table_description.table
    basis = table_description.basis
    opt = table_description.opt

    if opt == "min":
        table[-1] = -table[-1]
        table[-1][0] = -table[-1][0]

    while True:
        b = table[:-1, 0]

        new_basis_element_index = list(enumerate(table[-1][1:]))
        new_basis_element_index.sort(key=lambda t: t[1], reverse=True)
        new_basis_element_index = list(map(lambda t: t[0] + 1, new_basis_element_index))

        for new_basis_element in new_basis_element_index:
            borders = list(table[:-1, new_basis_element])
            for i in range(len(borders)):
                if borders[i] <= 0:
                    borders[i] = INF
                else:
                    borders[i] = b[i] / borders[i]
            old_basis_element = np.argmin(borders)

            if borders[old_basis_element] != INF:
                break

        if render_info:
            print(basis)
            print('%d --> %d' % (basis[old_basis_element], new_basis_element))
            print(table)
            print()

        if table[-1][new_basis_element] <= EPS:
            break

        if borders[old_basis_element] == INF:
            print("Infinity solutions")
            break

        table[old_basis_element] = table[old_basis_element] / table[old_basis_element][new_basis_element]
        for line in range(len(table)):
            if line == old_basis_element:
                continue

            table[line] = table[line] - table[line][new_basis_element] * table[old_basis_element]

        basis[old_basis_element] = new_basis_element

    f_opt = table[-1][0] if opt == "min" else -table[-1][0]
    x_opt = [0 for _ in range(table_description.original_vars_count)]

    for b_i, variable_index in zip(b, basis):
        if variable_index - 1 < table_description.original_vars_count:
            x_opt[variable_index - 1] = b_i

    return f_opt, x_opt
