# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [18, 54, 14]


def func2():
    return 66


def func3():
    return 72.16


def func4():
    return (16, 37, 15)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
