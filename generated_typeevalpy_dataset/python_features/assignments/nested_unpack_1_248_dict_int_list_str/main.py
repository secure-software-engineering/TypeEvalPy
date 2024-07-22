# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'urrwd': 2, 'xibzy': 80, 'ahwge': 67}


def func2():
    return 42


def func3():
    return [23, 93, 65]


def func4():
    return 'eatou'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
