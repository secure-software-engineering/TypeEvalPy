# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 37


def func2():
    return {'ceski': 59, 'sqdua': 31, 'kbjwh': 1}


def func3():
    return 89.79


def func4():
    return 'flnjr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
