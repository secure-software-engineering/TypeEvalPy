# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 54.28


def func2():
    return 24


def func3():
    return (8, 36, 100)


def func4():
    return {'rchun': 55, 'pkram': 37, 'blkqy': 87}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
