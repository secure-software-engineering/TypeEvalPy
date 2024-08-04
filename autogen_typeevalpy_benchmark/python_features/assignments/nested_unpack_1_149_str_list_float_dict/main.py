# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'eeuxr'


def func2():
    return [15, 30, 95]


def func3():
    return 51.37


def func4():
    return {'bwgmj': 35, 'dywox': 10, 'tkiks': 74}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
