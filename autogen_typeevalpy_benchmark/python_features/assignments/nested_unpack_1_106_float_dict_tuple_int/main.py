# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 82.02


def func2():
    return {'gwznk': 49, 'hopte': 68, 'robiq': 41}


def func3():
    return (90, 54, 53)


def func4():
    return 20


(a, b), (c, d) = [(func1, func2), (func3, func4)]
