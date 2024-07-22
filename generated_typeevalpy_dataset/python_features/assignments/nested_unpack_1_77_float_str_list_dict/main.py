# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 65.17


def func2():
    return 'jweza'


def func3():
    return [57, 75, 43]


def func4():
    return {'acktb': 89, 'nyjxm': 55, 'cwaum': 93}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
