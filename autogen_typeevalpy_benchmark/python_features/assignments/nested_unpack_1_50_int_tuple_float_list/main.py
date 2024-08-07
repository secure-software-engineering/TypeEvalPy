# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 80


def func2():
    return (82, 75, 71)


def func3():
    return 71.5


def func4():
    return [49, 77, 68]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
