# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'wedtb': 64, 'isyhe': 64, 'xyata': 70}


def func2():
    return 'upmfr'


def func3():
    return 59


def func4():
    return 41.6


(a, b), (c, d) = [(func1, func2), (func3, func4)]
