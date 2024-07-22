# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 45


def func2():
    return 'lkaoi'


def func3():
    return {'nxggm': 63, 'dqany': 62, 'svbbq': 12}


def func4():
    return [13, 68, 48]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
