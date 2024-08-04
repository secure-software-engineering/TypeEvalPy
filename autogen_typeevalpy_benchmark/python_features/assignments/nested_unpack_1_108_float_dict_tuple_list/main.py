# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 80.66


def func2():
    return {'prffx': 51, 'hxfet': 31, 'ttxss': 71}


def func3():
    return (42, 100, 37)


def func4():
    return [49, 60, 69]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
