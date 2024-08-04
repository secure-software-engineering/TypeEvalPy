# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 32.06


def func2():
    return [23, 59, 69]


def func3():
    return (44, 70, 46)


def func4():
    return 87


(a, b), (c, d) = [(func1, func2), (func3, func4)]
