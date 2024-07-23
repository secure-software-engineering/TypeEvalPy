# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'lkvxr'


def func2():
    return {'qjsav': 44, 'ydspq': 55, 'qydjr': 25}


def func3():
    return 11.72


def func4():
    return [68, 54, 88]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
