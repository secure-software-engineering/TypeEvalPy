# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'xjgqt'


def func2():
    return [36, 58, 70]


def func3():
    return 84.33


def func4():
    return 90


(a, b), (c, d) = [(func1, func2), (func3, func4)]
