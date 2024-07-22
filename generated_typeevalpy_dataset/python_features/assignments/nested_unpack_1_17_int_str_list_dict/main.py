# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48


def func2():
    return 'lzzrz'


def func3():
    return [8, 6, 9]


def func4():
    return {'ovfsy': 45, 'itqfp': 82, 'gkpup': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
