# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (63, 65, 68)


def func2():
    return 16


def func3():
    return 'mnvxl'


def func4():
    return 37.45


(a, b), (c, d) = [(func1, func2), (func3, func4)]
