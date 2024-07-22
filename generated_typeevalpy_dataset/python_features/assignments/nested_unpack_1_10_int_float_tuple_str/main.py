# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 91


def func2():
    return 64.83


def func3():
    return (41, 25, 85)


def func4():
    return 'deevx'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
