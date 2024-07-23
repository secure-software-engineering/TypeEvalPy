# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [72, 8, 14]


def func2():
    return {'wppux': 50, 'tavwg': 9, 'nrukk': 32}


def func3():
    return 'owrrv'


def func4():
    return 81


(a, b), (c, d) = [(func1, func2), (func3, func4)]
