# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jcksx': 98, 'qrlji': 60, 'ftvcx': 73}


def func2():
    return 'dvxml'


def func3():
    return (88, 83, 91)


def func4():
    return 99


(a, b), (c, d) = [(func1, func2), (func3, func4)]
