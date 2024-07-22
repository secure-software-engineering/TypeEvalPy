# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'lwasc'


def func2():
    return {'ntclj': 81, 'tmlqc': 90, 'glatd': 96}


def func3():
    return 92.77


def func4():
    return (4, 18, 75)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
