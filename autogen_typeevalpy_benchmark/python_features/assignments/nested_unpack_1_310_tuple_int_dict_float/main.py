# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (89, 6, 39)


def func2():
    return 58


def func3():
    return {'kgdnq': 2, 'lxdcd': 71, 'funht': 84}


def func4():
    return 90.07


(a, b), (c, d) = [(func1, func2), (func3, func4)]
