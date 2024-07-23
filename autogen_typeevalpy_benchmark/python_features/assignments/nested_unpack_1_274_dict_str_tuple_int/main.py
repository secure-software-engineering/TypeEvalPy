# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'dloll': 78, 'dglar': 11, 'ytzku': 29}


def func2():
    return 'wrcsx'


def func3():
    return (98, 70, 74)


def func4():
    return 16


(a, b), (c, d) = [(func1, func2), (func3, func4)]
