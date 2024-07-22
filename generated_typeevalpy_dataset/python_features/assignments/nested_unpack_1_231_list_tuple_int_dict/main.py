# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [6, 64, 23]


def func2():
    return (60, 83, 26)


def func3():
    return 94


def func4():
    return {'kkrxs': 74, 'pexoq': 4, 'xfmbh': 96}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
