# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'wdtjg'


def func2():
    return 94


def func3():
    return 55.93


def func4():
    return {'gozfa': 78, 'nsfbz': 63, 'jmbgd': 60}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
