# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (32, 96, 57)


def func2():
    return 53


def func3():
    return {'mgsde': 72, 'smleo': 37, 'oaxmz': 74}


def func4():
    return 22.31


(a, b), (c, d) = [(func1, func2), (func3, func4)]
