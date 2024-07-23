# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48.35


def func2():
    return {'wynnb': 25, 'odimk': 36, 'gburl': 73}


def func3():
    return 'qbayt'


def func4():
    return [79, 33, 69]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
