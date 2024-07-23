# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [53, 36, 41]


def func2():
    return 'typyc'


def func3():
    return 94.42


def func4():
    return 84


(a, b), (c, d) = [(func1, func2), (func3, func4)]
