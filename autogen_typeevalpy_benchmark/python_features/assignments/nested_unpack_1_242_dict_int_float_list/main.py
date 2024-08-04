# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'umjsa': 2, 'ctdgk': 16, 'oexgj': 99}


def func2():
    return 92


def func3():
    return 25.65


def func4():
    return [99, 57, 32]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
