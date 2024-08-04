# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 29


def func2():
    return 'udbzp'


def func3():
    return 77.08


def func4():
    return {'lxosj': 60, 'kdrxw': 7, 'xufus': 72}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
