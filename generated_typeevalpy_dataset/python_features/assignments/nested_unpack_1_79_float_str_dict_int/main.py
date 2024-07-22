# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 7.31


def func2():
    return 'qadkw'


def func3():
    return {'kejmq': 47, 'wpvof': 57, 'dtlvl': 26}


def func4():
    return 13


(a, b), (c, d) = [(func1, func2), (func3, func4)]
