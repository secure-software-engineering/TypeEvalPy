# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 76.2


def func2():
    return (12, 52, 49)


def func3():
    return [49, 71, 61]


def func4():
    return 'baeml'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
