# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 6


def func2():
    return 31.52


def func3():
    return {'xuwxf': 23, 'gcuwk': 53, 'qeywz': 4}


def func4():
    return 'eyukr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
