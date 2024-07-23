# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [68, 47, 60]


def func2():
    return (9, 27, 28)


def func3():
    return 8


def func4():
    return 63.36


(a, b), (c, d) = [(func1, func2), (func3, func4)]
