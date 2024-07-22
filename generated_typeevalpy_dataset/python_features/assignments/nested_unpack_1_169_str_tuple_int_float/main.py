# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'hexaf'


def func2():
    return (52, 14, 32)


def func3():
    return 53


def func4():
    return 62.94


(a, b), (c, d) = [(func1, func2), (func3, func4)]