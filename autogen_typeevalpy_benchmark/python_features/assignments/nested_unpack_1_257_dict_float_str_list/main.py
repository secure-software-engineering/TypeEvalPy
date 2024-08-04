# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'wqgjz': 68, 'ciwne': 40, 'nlyag': 43}


def func2():
    return 49.5


def func3():
    return 'tarjh'


def func4():
    return [65, 36, 8]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
