# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [45, 59, 30]


def func2():
    return {'bqqzm': 67, 'zspbi': 94, 'mcyeq': 55}


def func3():
    return 23.39


def func4():
    return 31


(a, b), (c, d) = [(func1, func2), (func3, func4)]
