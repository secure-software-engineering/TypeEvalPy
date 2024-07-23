# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31


def func2():
    return [9, 75, 55]


def func3():
    return {'aulxa': 73, 'xmqtr': 1, 'fjtbk': 99}


def func4():
    return 'mfinw'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
