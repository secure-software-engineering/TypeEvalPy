# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [80, 83, 85]


def func2():
    return 69


def func3():
    return 78.16


def func4():
    return (47, 53, 46)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
