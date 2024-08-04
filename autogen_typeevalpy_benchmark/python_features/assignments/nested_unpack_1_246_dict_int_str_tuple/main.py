# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'nlvol': 50, 'untwq': 25, 'jqibz': 68}


def func2():
    return 88


def func3():
    return 'mopiq'


def func4():
    return (15, 13, 67)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
