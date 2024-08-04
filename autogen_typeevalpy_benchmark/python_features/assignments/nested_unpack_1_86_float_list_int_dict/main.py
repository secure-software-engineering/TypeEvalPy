# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 55.01


def func2():
    return [83, 39, 62]


def func3():
    return 32


def func4():
    return {'urhbb': 48, 'lmfpi': 66, 'stwzd': 72}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
