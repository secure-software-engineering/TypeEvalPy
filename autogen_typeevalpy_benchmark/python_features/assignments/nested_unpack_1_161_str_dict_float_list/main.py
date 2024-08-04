# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'qezsy'


def func2():
    return {'ufpeh': 79, 'rdsyy': 29, 'kzzap': 82}


def func3():
    return 56.99


def func4():
    return [64, 19, 43]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
