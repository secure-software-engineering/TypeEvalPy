# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'idhfb': 19, 'icwwq': 74, 'syzcr': 89}


def func2():
    return 'cqgka'


def func3():
    return [33, 87, 34]


def func4():
    return 83


(a, b), (c, d) = [(func1, func2), (func3, func4)]
