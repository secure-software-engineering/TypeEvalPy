# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (51, 43, 33)


def func2():
    return 'pyijx'


def func3():
    return 55.92


def func4():
    return {'ifbkd': 31, 'qxpoc': 60, 'dyvba': 50}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
