# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [48, 72, 72]


def func2():
    return {'mzpuk': 79, 'dwdfu': 90, 'ycnuu': 88}


def func3():
    return 'sezac'


def func4():
    return 19


(a, b), (c, d) = [(func1, func2), (func3, func4)]
