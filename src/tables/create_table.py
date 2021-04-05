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


def evaluate_function(old_vars_count, new_vars_count, constraints, function):
    x = [0 for _ in range(old_vars_count + new_vars_count)]

    for constraint in constraints:
        unit_vector = constraint[old_vars_count:-2]
        index_at_eye = np.argmax(unit_vector)

        if unit_vector[index_at_eye] == 1:
            x[old_vars_count + index_at_eye] = constraint[-1]

    return np.array(function) @ np.array(x)


# constrains is list like: [a_i_1, .., a_i_m, ###, b_i], where ### is "==" or "<=" or ">="
# function   is list like: [c_1, .., c_m]
def create_table(constraints, function):
    constraints = list(map(change_ge_to_le, constraints))

    old_vars_count = len(function)
    new_vars_count = less_or_equals_count(constraints)
    add_new_variables(constraints, new_vars_count)
    function.extend([0 for _ in range(new_vars_count)])

    f_at_x0 = evaluate_function(old_vars_count, new_vars_count, constraints, function)
    function.insert(0, f_at_x0)

    constraints = list(map(to_table_format, constraints))
    table = np.array([*constraints, function], dtype='float32')
    basic = np.array([i for i in range(old_vars_count + 1, old_vars_count + 1 + new_vars_count)])

    return table, basic
