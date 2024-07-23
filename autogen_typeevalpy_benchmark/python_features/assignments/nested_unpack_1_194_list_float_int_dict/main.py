# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [81, 74, 50]


def func2():
    return 8.07


def func3():
    return 2


def func4():
    return {'nnfos': 73, 'xbxlb': 65, 'fribq': 20}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
