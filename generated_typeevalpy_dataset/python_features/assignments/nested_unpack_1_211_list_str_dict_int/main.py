# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [3, 68, 69]


def func2():
    return 'wbrqm'


def func3():
    return {'mrazo': 50, 'podoe': 17, 'pwphz': 17}


def func4():
    return 92


(a, b), (c, d) = [(func1, func2), (func3, func4)]
