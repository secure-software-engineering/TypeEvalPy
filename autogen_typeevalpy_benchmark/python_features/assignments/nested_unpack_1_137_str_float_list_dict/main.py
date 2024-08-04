# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'dwgsv'


def func2():
    return 76.39


def func3():
    return [87, 51, 63]


def func4():
    return {'dqqjb': 94, 'utkts': 12, 'wlmpw': 94}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
