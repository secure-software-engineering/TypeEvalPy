# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (89, 86, 31)


def func2():
    return [33, 71, 50]


def func3():
    return 'iyjvd'


def func4():
    return 86.83


(a, b), (c, d) = [(func1, func2), (func3, func4)]
