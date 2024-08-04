# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [23, 54, 64]


def func2():
    return (18, 81, 67)


def func3():
    return 53.86


def func4():
    return 'imgwb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
