# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (86, 90, 68)


def func2():
    return 71


def func3():
    return [57, 59, 39]


def func4():
    return 57.16


(a, b), (c, d) = [(func1, func2), (func3, func4)]
