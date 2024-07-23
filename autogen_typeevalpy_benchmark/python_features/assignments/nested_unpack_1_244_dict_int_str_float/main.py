# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'czerx': 84, 'vyibm': 51, 'fafzo': 93}


def func2():
    return 22


def func3():
    return 'pjpex'


def func4():
    return 68.51


(a, b), (c, d) = [(func1, func2), (func3, func4)]
