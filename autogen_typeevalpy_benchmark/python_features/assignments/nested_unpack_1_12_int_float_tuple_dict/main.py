# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 95


def func2():
    return 54.9


def func3():
    return (24, 38, 77)


def func4():
    return {'ioklz': 34, 'vcitn': 36, 'fxxyz': 98}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
