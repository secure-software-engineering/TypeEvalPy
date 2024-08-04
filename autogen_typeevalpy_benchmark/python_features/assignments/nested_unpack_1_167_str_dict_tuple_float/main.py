# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'coown'


def func2():
    return {'xaspu': 45, 'cdopz': 53, 'ccuuw': 34}


def func3():
    return (50, 84, 63)


def func4():
    return 57.63


(a, b), (c, d) = [(func1, func2), (func3, func4)]
