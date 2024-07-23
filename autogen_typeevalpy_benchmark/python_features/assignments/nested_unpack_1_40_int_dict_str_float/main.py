# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 71


def func2():
    return {'jdrbj': 61, 'dfvaj': 59, 'xomcv': 17}


def func3():
    return 'relwg'


def func4():
    return 22.99


(a, b), (c, d) = [(func1, func2), (func3, func4)]
