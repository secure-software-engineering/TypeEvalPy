# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'vqhcn': 58, 'whdhw': 48, 'acepd': 23}


def func2():
    return [34, 90, 31]


def func3():
    return 'muwic'


def func4():
    return 19


(a, b), (c, d) = [(func1, func2), (func3, func4)]
