# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 28


def func2():
    return 43.38


def func3():
    return [55, 95, 34]


def func4():
    return {'deyxk': 28, 'fyobu': 70, 'foljx': 90}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
