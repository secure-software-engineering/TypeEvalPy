# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 87


def func2():
    return 53.06


def func3():
    return 'bujls'


def func4():
    return (17, 3, 64)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
