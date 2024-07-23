# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'jrrap'


def func2():
    return 65.92


def func3():
    return {'oosgy': 12, 'uezku': 17, 'cakjh': 83}


def func4():
    return (95, 39, 29)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
