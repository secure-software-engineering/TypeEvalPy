# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 71.27


def func2():
    return [31, 67, 75]


def func3():
    return (17, 70, 39)


def func4():
    return 'eowji'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
