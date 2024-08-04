# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 12.76


def func2():
    return [13, 51, 48]


def func3():
    return {'uiytf': 79, 'nnbdi': 41, 'mlpni': 21}


def func4():
    return 51


(a, b), (c, d) = [(func1, func2), (func3, func4)]
