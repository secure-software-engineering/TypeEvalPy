# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'omnid'


def func2():
    return 52.85


def func3():
    return {'rirca': 44, 'tvbqx': 59, 'vrwcr': 28}


def func4():
    return 15


(a, b), (c, d) = [(func1, func2), (func3, func4)]
