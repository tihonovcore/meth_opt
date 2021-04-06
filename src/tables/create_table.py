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
        self.basic = None

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
    basic_vector_index = 0

    for constraint in constraints:
        new_vars_coefficients = [0 for _ in range(new_vars_count)]
        new_vars_coefficients[basic_vector_index] = 1
        basic_vector_index += 1

        for coef in new_vars_coefficients:
            constraint.insert(-2, coef)


def to_table_format(constraint):
    return [constraint[-1], *constraint[:-2]]


def evaluate_function(old_vars_count, new_vars_count, constraints, function):
    x = [0 for _ in range(old_vars_count + new_vars_count)]

    if new_vars_count == 0:
        return np.array(function) @ np.array(x)

    for constraint in constraints:
        unit_vector = constraint[old_vars_count:-2]
        index_at_eye = np.argmax(unit_vector)

        if unit_vector[index_at_eye] == 1:
            x[old_vars_count + index_at_eye] = constraint[-1]

    return np.array(function) @ np.array(x)


def choose_basic(constraints, old_vars_count, new_vars_count):
    rank, _ = constraints.shape

    if rank == new_vars_count:
        # todo: if f((b, 0)) is not >= 0 this don't work!!!
        #  needs another basis
        return [i for i in range(old_vars_count + 1, old_vars_count + 1 + new_vars_count)]

    raise Exception('rank(%d) != new_vars_count(%d)' % (rank, new_vars_count))


def create_simplex_table(table_description):
    constraints = table_description.constraints
    function = table_description.function

    constraints = list(map(change_ge_to_le, constraints))

    old_vars_count = len(function)
    new_vars_count = len(constraints)
    add_new_variables(constraints, new_vars_count)
    function.extend([0 for _ in range(new_vars_count)])

    f_at_x0 = evaluate_function(old_vars_count, new_vars_count, constraints, function)
    function.insert(0, f_at_x0)

    constraints = np.array(list(map(to_table_format, constraints)), dtype='float32')
    basic = choose_basic(constraints, old_vars_count, new_vars_count)
    table = np.concatenate((constraints, [function]))

    table_description.table = table
    table_description.basic = basic
