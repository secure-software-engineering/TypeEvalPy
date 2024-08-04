# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [83, 36, 28]


def func2():
    return {'depvr': 76, 'kicrm': 21, 'pqkgd': 18}


def func3():
    return 81


def func4():
    return 'nxdex'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
