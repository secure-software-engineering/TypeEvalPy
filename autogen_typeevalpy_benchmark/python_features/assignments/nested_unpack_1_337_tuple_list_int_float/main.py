# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (31, 20, 96)


def func2():
    return [88, 98, 39]


def func3():
    return 56


def func4():
    return 41.62


(a, b), (c, d) = [(func1, func2), (func3, func4)]
