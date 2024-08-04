# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'gjxek'


def func2():
    return 31.25


def func3():
    return {'sgrsa': 10, 'mdfra': 30, 'svzkd': 50}


def func4():
    return [12, 94, 14]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
