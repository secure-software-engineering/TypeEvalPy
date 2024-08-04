# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 87


def func2():
    return 98.13


def func3():
    return {'nycze': 33, 'zgcls': 6, 'ipnko': 91}


def func4():
    return (56, 1, 67)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
