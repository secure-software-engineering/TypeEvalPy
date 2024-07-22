# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [92, 88, 32]


def func2():
    return 61.13


def func3():
    return {'wskna': 72, 'rjzay': 47, 'eyxdt': 53}


def func4():
    return 'hfyed'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
