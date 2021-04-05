import numpy as np


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
        if constraint[-2] == "<=":
            new_vars_coefficients = [0 for _ in range(new_vars_count)]
            new_vars_coefficients[basic_vector_index] = 1
            basic_vector_index += 1

            for coef in new_vars_coefficients:
                constraint.insert(-2, coef)

            constraint[-2] = "=="
        elif constraint[-2] == "==":
            for j in range(new_vars_count):
                constraint.insert(-2, 0)
        else:
            msg = "here expected '<=' or '==', but not '%s'" % constraint[-2]
            raise Exception(msg)


def to_table_format(constraint):
    return [constraint[-1], *constraint[:-2]]


# constrains is list like: [a_i_1, .., a_i_m, ###, b_i], where ### is "==" or "<=" or ">="
# function   is list like: [c_1, .., c_m]
def create_table(constraints, function):
    constraints = list(map(change_ge_to_le, constraints))

    old_vars_count = len(function) + 1
    new_vars_count = less_or_equals_count(constraints)
    add_new_variables(constraints, new_vars_count)
    function.extend([0 for _ in range(new_vars_count)])

    # todo: find x_0 and evaluate f(x_0)
    function.insert(0, 0)

    constraints = list(map(to_table_format, constraints))
    table = np.array([*constraints, function], dtype='float32')
    basic = np.array([i for i in range(old_vars_count, old_vars_count + new_vars_count)])

    return table, basic
