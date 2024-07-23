# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'fianl': 30, 'zthtl': 64, 'xfjnw': 10}


def func2():
    return 53


def func3():
    return [2, 57, 14]


def func4():
    return 12.26


(a, b), (c, d) = [(func1, func2), (func3, func4)]
