# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 28.05


def func2():
    return 'jtttz'


def func3():
    return [6, 66, 6]


def func4():
    return 36


(a, b), (c, d) = [(func1, func2), (func3, func4)]
