# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [34, 62, 15]


def func2():
    return 71.85


def func3():
    return 'dmcxp'


def func4():
    return 2


(a, b), (c, d) = [(func1, func2), (func3, func4)]
