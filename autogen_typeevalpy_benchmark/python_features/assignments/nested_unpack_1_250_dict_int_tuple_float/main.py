# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'oftyg': 29, 'zlksz': 28, 'pnzhh': 41}


def func2():
    return 3


def func3():
    return (99, 89, 36)


def func4():
    return 91.99


(a, b), (c, d) = [(func1, func2), (func3, func4)]
