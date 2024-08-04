# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [31, 95, 31]


def func2():
    return {'wffgq': 80, 'ecxrr': 41, 'ptobm': 64}


def func3():
    return (74, 36, 63)


def func4():
    return 'etnkt'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
