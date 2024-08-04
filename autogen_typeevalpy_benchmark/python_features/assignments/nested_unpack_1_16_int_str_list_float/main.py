# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 79


def func2():
    return 'vxlxl'


def func3():
    return [21, 96, 61]


def func4():
    return 45.56


(a, b), (c, d) = [(func1, func2), (func3, func4)]
