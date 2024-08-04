# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'drzzt': 52, 'oclud': 65, 'imtog': 56}


def func2():
    return 77.61


def func3():
    return 17


def func4():
    return 'tmfko'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
