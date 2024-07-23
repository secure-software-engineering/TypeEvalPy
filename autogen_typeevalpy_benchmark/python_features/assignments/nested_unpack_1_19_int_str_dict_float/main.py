# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31


def func2():
    return 'volkf'


def func3():
    return {'bvxxg': 10, 'hcnkf': 95, 'xiwhz': 66}


def func4():
    return 23.19


(a, b), (c, d) = [(func1, func2), (func3, func4)]
