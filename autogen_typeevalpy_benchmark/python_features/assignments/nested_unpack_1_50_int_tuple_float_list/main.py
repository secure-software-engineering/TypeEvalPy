# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 64


def func2():
    return (30, 75, 3)


def func3():
    return 62.64


def func4():
    return [43, 56, 22]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
