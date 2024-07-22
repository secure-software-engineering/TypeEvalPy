# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'saiwb'


def func2():
    return 99.44


def func3():
    return [15, 24, 71]


def func4():
    return 19


(a, b), (c, d) = [(func1, func2), (func3, func4)]
