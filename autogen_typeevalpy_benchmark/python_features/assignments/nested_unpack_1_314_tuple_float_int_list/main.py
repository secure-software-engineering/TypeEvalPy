# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (53, 82, 35)


def func2():
    return 42.04


def func3():
    return 72


def func4():
    return [60, 91, 73]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
