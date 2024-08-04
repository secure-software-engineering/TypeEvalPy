# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'pvvtk': 60, 'jrsep': 52, 'vbgvb': 61}


def func2():
    return [39, 61, 96]


def func3():
    return 'yxgrk'


def func4():
    return 27.0


(a, b), (c, d) = [(func1, func2), (func3, func4)]
