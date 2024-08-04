# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 99.07


def func2():
    return [95, 39, 76]


def func3():
    return {'ivnsh': 84, 'vjrzp': 100, 'usram': 75}


def func4():
    return 'pspeq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
