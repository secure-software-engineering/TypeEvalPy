# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kyssq'


def func2():
    return {'ficca': 59, 'fnfbp': 96, 'izgls': 31}


def func3():
    return [87, 11, 4]


def func4():
    return 57.87


(a, b), (c, d) = [(func1, func2), (func3, func4)]
