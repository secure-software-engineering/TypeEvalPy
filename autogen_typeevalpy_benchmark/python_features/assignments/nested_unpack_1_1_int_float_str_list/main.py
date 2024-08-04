# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 8


def func2():
    return 96.12


def func3():
    return 'ceprg'


def func4():
    return [16, 73, 32]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
