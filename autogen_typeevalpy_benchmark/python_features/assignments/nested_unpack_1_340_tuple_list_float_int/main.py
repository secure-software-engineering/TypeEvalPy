# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (82, 16, 96)


def func2():
    return [84, 56, 31]


def func3():
    return 7.53


def func4():
    return 15


(a, b), (c, d) = [(func1, func2), (func3, func4)]
