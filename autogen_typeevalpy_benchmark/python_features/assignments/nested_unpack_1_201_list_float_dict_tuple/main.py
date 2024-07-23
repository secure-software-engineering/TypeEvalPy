# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [47, 11, 70]


def func2():
    return 78.08


def func3():
    return {'qpijb': 83, 'cnzvd': 56, 'cnvth': 7}


def func4():
    return (73, 94, 54)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
