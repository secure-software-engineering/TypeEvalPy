# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [63, 64, 24]


def func2():
    return {'ooudp': 45, 'snmlt': 20, 'lvplg': 43}


def func3():
    return 'fxjpg'


def func4():
    return 26


(a, b), (c, d) = [(func1, func2), (func3, func4)]
