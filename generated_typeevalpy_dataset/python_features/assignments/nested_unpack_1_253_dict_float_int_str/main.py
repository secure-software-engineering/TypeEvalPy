# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'dulqa': 77, 'zgble': 41, 'wvont': 49}


def func2():
    return 79.76


def func3():
    return 12


def func4():
    return 'eqokl'


(a, b), (c, d) = [(func1, func2), (func3, func4)]