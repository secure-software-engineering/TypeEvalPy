# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 57.82


def func2():
    return 'nkqgc'


def func3():
    return {'tmkog': 57, 'glzhx': 12, 'mdwlx': 88}


def func4():
    return [41, 86, 45]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
