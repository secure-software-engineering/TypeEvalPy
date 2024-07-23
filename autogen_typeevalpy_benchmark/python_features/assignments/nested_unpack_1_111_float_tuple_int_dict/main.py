# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 36.81


def func2():
    return (58, 11, 28)


def func3():
    return 12


def func4():
    return {'mgwlr': 99, 'ztizz': 50, 'fmkin': 56}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
