# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (4, 39, 14)


def func2():
    return {'adxbb': 27, 'efqrk': 4, 'fejme': 63}


def func3():
    return 1


def func4():
    return [83, 58, 44]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
