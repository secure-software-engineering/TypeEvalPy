# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'quxwt': 43, 'xpzrf': 50, 'arzqr': 60}


def func2():
    return [45, 55, 57]


def func3():
    return 39


def func4():
    return (8, 45, 27)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
