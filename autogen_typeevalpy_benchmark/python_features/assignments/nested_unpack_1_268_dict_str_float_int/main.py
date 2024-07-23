# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'frvjh': 68, 'dxqxj': 26, 'semuj': 34}


def func2():
    return 'ahorf'


def func3():
    return 13.9


def func4():
    return 25


(a, b), (c, d) = [(func1, func2), (func3, func4)]
