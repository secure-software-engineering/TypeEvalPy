# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 61.49


def func2():
    return 'ssmnj'


def func3():
    return {'zlahy': 29, 'moisp': 20, 'elpoa': 73}


def func4():
    return 24


(a, b), (c, d) = [(func1, func2), (func3, func4)]
