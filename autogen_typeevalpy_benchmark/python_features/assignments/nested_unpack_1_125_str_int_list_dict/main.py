# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'bwurd'


def func2():
    return 39


def func3():
    return [31, 33, 85]


def func4():
    return {'eljlp': 11, 'pnywk': 14, 'azsvp': 99}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
