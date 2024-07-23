# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 39


def func2():
    return 'posdi'


def func3():
    return [9, 49, 54]


def func4():
    return 69.76


(a, b), (c, d) = [(func1, func2), (func3, func4)]
