# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'wqche'


def func2():
    return (33, 68, 41)


def func3():
    return 38.29


def func4():
    return {'twstg': 96, 'vncmm': 57, 'qguve': 88}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
