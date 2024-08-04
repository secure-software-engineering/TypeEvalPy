# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 22


def func2():
    return 'rhrqc'


def func3():
    return 95.25


def func4():
    return [31, 87, 40]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
