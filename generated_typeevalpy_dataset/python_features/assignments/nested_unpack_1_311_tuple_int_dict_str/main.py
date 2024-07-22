# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (72, 16, 72)


def func2():
    return 8


def func3():
    return {'dvelz': 87, 'pohkz': 49, 'jmybx': 8}


def func4():
    return 'djiiq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
