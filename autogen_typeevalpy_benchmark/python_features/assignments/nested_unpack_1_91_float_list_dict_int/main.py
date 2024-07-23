# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 99.38


def func2():
    return [82, 50, 23]


def func3():
    return {'rxdjv': 95, 'wgqvv': 84, 'aqepg': 4}


def func4():
    return 21


(a, b), (c, d) = [(func1, func2), (func3, func4)]
