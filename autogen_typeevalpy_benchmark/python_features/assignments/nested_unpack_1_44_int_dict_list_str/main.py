# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 60


def func2():
    return {'qctyp': 33, 'oqmue': 51, 'jqznb': 11}


def func3():
    return [56, 77, 30]


def func4():
    return 'dwtyt'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
