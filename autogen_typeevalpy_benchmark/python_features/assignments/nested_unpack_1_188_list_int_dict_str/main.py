# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [62, 73, 87]


def func2():
    return 57


def func3():
    return {'ejjar': 87, 'vzdxc': 68, 'kbgis': 99}


def func4():
    return 'tsfyw'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
