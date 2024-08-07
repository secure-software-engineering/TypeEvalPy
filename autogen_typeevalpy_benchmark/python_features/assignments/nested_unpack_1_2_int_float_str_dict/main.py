# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 75


def func2():
    return 59.86


def func3():
    return 'qkpny'


def func4():
    return {'fsgkr': 45, 'hitbl': 9, 'zzbfg': 32}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
