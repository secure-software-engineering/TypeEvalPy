# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [39, 19, 59]


def func2():
    return 25


def func3():
    return (67, 67, 24)


def func4():
    return 8.92


(a, b), (c, d) = [(func1, func2), (func3, func4)]
