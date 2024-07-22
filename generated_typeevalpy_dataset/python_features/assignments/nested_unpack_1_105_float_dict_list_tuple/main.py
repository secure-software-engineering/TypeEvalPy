# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 47.51


def func2():
    return {'ndtgf': 52, 'pvexg': 29, 'uqwfy': 99}


def func3():
    return [41, 9, 33]


def func4():
    return (13, 43, 61)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
