import numpy as np


class TableDescription:
    # constrains is list like: [a_i_1, .., a_i_m, ###, b_i], where ### is "==" or "<=" or ">="
    # function   is list like: [c_1, .., c_m]
    def __init__(self, constraints, function, opt, description=""):
        self.constraints = constraints
        self.function = function
        self.opt = opt
        self.description = description

        self.table = None
        self.basis = None

        self.original_vars_count = len(function)


def change_ge_to_le(constraint):
    if constraint[-2] != ">=":
        return constraint

    n = len(constraint)
    for i in range(n):
        if i == n - 2:
            constraint[i] = "<="
        else:
            constraint[i] = -constraint[i]

    return constraint


def less_or_equals_count(constraints):
    return sum(list(map(lambda t: 1 if t[-2] == "<=" else 0, constraints)))


def add_new_variables(constraints, new_vars_count):
    basis_vector_index = 0

    for constraint in constraints:
        new_vars_coefficients = [0 for _ in range(new_vars_count)]
        new_vars_coefficients[basis_vector_index] = 1
        basis_vector_index += 1

        for coef in new_vars_coefficients:
            constraint.insert(-2, coef)


def to_table_format(constraint):
    return [constraint[-1], *constraint[:-2]]


def rank_by_occurs(constraints, occurs):
    matrix = constraints[:, occurs]
    return np.linalg.matrix_rank(matrix)


def gauss(constraints, occurs):
    n, _ = constraints.shape

    for i, o in enumerate(occurs):
        if constraints[i][o] == 0:
            for j in range(i + 1, n):
                if constraints[j][o] != 0:
                    constraints[i] += constraints[j]
                    break

        constraints[i] /= constraints[i][o]

        for j in range(i + 1, n):
            constraints[j] -= constraints[i] * constraints[j][o]

    for i, o in reversed(list(enumerate(occurs))):
        for j in range(i):
            constraints[j] -= constraints[i] * constraints[j][o]


def choose_basis(constraints, old_vars_count, new_vars_count):
    rank, _ = constraints.shape
    if rank != new_vars_count:
        raise Exception('rank(%d) != new_vars_count(%d)' % (rank, new_vars_count))

    b = constraints[:, 0]
    if all(b >= 0):
        return [i for i in range(old_vars_count + 1, old_vars_count + 1 + new_vars_count)]

    for i in range(2 ** (old_vars_count + new_vars_count)):
        occurs = [j + 1 for j, x in enumerate(list(reversed(bin(i)[2:]))) if x == '1']
        if len(occurs) != rank:
            continue

        if rank_by_occurs(constraints, occurs) == rank:
            gauss(constraints, occurs)

            b = constraints[:, 0]
            if all(b >= 0):
                return occurs

    raise Exception("there is no basis")


def create_simplex_table(table_description):
    constraints = table_description.constraints
    function = table_description.function

    constraints = list(map(change_ge_to_le, constraints))

    old_vars_count = len(function)
    new_vars_count = len(constraints)
    add_new_variables(constraints, new_vars_count)
    function.extend([0 for _ in range(new_vars_count)])

    constraints = np.array(list(map(to_table_format, constraints)), dtype='float32')
    basis = choose_basis(constraints, old_vars_count, new_vars_count)

    function.insert(0, 0)
    table = np.concatenate((constraints, [function]))

    table_description.table = table
    table_description.basis = basis
