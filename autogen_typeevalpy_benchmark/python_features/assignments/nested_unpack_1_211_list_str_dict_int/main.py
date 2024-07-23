# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [49, 7, 78]


def func2():
    return 'lfaio'


def func3():
    return {'ijlbj': 71, 'yynks': 4, 'qljyx': 72}


def func4():
    return 26


(a, b), (c, d) = [(func1, func2), (func3, func4)]
