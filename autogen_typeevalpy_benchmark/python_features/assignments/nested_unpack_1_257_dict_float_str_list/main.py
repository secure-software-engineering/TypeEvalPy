# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'nphsa': 50, 'ofnsj': 53, 'wwigq': 91}


def func2():
    return 10.04


def func3():
    return 'aeqgf'


def func4():
    return [9, 17, 48]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
