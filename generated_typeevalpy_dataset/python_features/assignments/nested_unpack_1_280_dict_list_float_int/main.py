# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'yvxxz': 11, 'ylmdc': 50, 'kobcv': 80}


def func2():
    return [99, 72, 99]


def func3():
    return 39.51


def func4():
    return 48


(a, b), (c, d) = [(func1, func2), (func3, func4)]
