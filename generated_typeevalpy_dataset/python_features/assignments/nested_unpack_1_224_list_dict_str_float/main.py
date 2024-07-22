# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [37, 85, 14]


def func2():
    return {'upyor': 89, 'tbnek': 55, 'wfjoa': 17}


def func3():
    return 'cbdsm'


def func4():
    return 56.32


(a, b), (c, d) = [(func1, func2), (func3, func4)]
