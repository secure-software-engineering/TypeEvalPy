# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'eprap'


def func2():
    return 52


def func3():
    return 56.26


def func4():
    return [83, 36, 95]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
