# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 87.92


def func2():
    return 'uqezl'


def func3():
    return (8, 16, 67)


def func4():
    return [20, 39, 22]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
