# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [12, 10, 7]


def func2():
    return 'egbvx'


def func3():
    return 41.36


def func4():
    return 58


(a, b), (c, d) = [(func1, func2), (func3, func4)]
