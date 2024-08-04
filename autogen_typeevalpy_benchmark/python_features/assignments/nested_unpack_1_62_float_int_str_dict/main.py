# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 46.71


def func2():
    return 5


def func3():
    return 'bvbww'


def func4():
    return {'pnmou': 44, 'xlvqi': 92, 'mdbcx': 11}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
