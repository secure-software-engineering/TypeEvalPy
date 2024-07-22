# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [7, 27, 38]


def func2():
    return 24


def func3():
    return 'wsmxf'


def func4():
    return {'infuk': 65, 'ombor': 64, 'baxiv': 32}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
