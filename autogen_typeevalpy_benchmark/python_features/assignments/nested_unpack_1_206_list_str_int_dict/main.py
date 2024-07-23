# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [90, 22, 13]


def func2():
    return 'dfudv'


def func3():
    return 3


def func4():
    return {'evejk': 44, 'kbdps': 22, 'kevmt': 48}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
