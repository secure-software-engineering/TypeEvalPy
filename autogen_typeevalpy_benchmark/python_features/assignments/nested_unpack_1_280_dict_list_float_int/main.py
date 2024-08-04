# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'lzcqk': 78, 'luple': 1, 'nolje': 74}


def func2():
    return [64, 94, 31]


def func3():
    return 71.5


def func4():
    return 35


(a, b), (c, d) = [(func1, func2), (func3, func4)]
