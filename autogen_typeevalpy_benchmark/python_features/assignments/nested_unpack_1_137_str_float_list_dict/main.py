# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'mjbte'


def func2():
    return 51.93


def func3():
    return [96, 8, 32]


def func4():
    return {'lbsiu': 8, 'shrge': 79, 'jekdr': 83}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
