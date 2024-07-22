# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 11


def func2():
    return {'tlryd': 95, 'rnxge': 39, 'xxtwz': 54}


def func3():
    return [7, 18, 37]


def func4():
    return 'ncraw'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
