# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'oesfn'


def func2():
    return (61, 86, 46)


def func3():
    return [65, 39, 22]


def func4():
    return {'vwecd': 43, 'gvter': 48, 'icjth': 34}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
