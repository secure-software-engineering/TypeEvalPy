# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 63.2


def func2():
    return [82, 36, 16]


def func3():
    return {'zxfiy': 15, 'rtyqp': 64, 'unxwc': 73}


def func4():
    return 25


(a, b), (c, d) = [(func1, func2), (func3, func4)]
