# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'abgdt': 29, 'gzqzh': 23, 'cralf': 97}


def func2():
    return 'isghx'


def func3():
    return 42


def func4():
    return 98.63


(a, b), (c, d) = [(func1, func2), (func3, func4)]
