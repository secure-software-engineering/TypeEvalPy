# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 71.24


def func2():
    return 'ohhes'


def func3():
    return {'sejfz': 51, 'ugmjo': 92, 'mzdwb': 93}


def func4():
    return (62, 68, 53)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
