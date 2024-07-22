# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [46, 56, 49]


def func2():
    return {'mnlzq': 14, 'tgsmy': 40, 'zqmck': 50}


def func3():
    return 53.19


def func4():
    return 14


(a, b), (c, d) = [(func1, func2), (func3, func4)]
