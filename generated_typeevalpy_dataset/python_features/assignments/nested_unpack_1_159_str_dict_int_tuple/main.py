# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'hwlri'


def func2():
    return {'fxypk': 31, 'gkjdt': 26, 'swstw': 4}


def func3():
    return 28


def func4():
    return (79, 16, 24)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
