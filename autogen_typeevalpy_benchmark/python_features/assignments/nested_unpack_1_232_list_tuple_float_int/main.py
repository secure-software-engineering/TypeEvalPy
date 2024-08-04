# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [72, 56, 49]


def func2():
    return (26, 19, 95)


def func3():
    return 15.81


def func4():
    return 2


(a, b), (c, d) = [(func1, func2), (func3, func4)]
