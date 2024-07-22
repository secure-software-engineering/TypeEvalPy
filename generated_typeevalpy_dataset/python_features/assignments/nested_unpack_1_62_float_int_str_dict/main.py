# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 25.9


def func2():
    return 53


def func3():
    return 'emsaa'


def func4():
    return {'ionio': 27, 'tfavp': 71, 'pgppd': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
