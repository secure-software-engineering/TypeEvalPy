# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ibyub'


def func2():
    return 76.09


def func3():
    return [94, 18, 35]


def func4():
    return (20, 94, 68)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
