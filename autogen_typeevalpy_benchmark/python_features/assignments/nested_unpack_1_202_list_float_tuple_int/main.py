# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [83, 85, 86]


def func2():
    return 89.11


def func3():
    return (46, 11, 46)


def func4():
    return 72


(a, b), (c, d) = [(func1, func2), (func3, func4)]
