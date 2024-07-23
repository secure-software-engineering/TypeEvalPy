# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [37, 72, 78]


def func2():
    return 'tafyi'


def func3():
    return (8, 71, 91)


def func4():
    return 81


(a, b), (c, d) = [(func1, func2), (func3, func4)]
