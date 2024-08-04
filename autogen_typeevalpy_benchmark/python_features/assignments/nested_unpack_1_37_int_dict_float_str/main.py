# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 83


def func2():
    return {'vmsnh': 54, 'vzgoj': 44, 'xnwwh': 65}


def func3():
    return 27.45


def func4():
    return 'asvpr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
