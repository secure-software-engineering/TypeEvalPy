# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [92, 57, 59]


def func2():
    return 'qhzuf'


def func3():
    return {'wshpu': 36, 'nuhng': 26, 'sknms': 31}


def func4():
    return 41.44


(a, b), (c, d) = [(func1, func2), (func3, func4)]
