# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ntzhu': 32, 'bfjsf': 54, 'xzxdj': 71}


def func2():
    return 25.32


def func3():
    return 'jvabj'


def func4():
    return 41


(a, b), (c, d) = [(func1, func2), (func3, func4)]
