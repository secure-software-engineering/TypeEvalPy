# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 4.52


def func2():
    return 'zgmpx'


def func3():
    return 12


def func4():
    return {'fmwjd': 41, 'wgzfs': 83, 'abuvk': 75}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
