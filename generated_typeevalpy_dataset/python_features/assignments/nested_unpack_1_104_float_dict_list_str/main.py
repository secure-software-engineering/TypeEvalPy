# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 7.18


def func2():
    return {'ootuy': 39, 'drlec': 43, 'cnzmm': 88}


def func3():
    return [19, 8, 49]


def func4():
    return 'butzr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
