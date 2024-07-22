# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 64


def func2():
    return [82, 90, 29]


def func3():
    return 'vwahk'


def func4():
    return {'diwlk': 33, 'eyunq': 42, 'nizqt': 38}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
