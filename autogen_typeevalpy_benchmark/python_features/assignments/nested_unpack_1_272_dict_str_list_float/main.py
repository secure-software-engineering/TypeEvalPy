# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'lfnjk': 79, 'wftrp': 13, 'cwgzb': 84}


def func2():
    return 'rvnew'


def func3():
    return [60, 49, 2]


def func4():
    return 67.33


(a, b), (c, d) = [(func1, func2), (func3, func4)]
