# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'qnncw'


def func2():
    return [46, 51, 14]


def func3():
    return {'nvzhx': 46, 'zlxka': 31, 'ksjvr': 36}


def func4():
    return (50, 73, 7)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
