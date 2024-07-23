# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 14.48


def func2():
    return 38


def func3():
    return [12, 19, 92]


def func4():
    return {'aqipb': 62, 'rsevu': 95, 'gkmpj': 95}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
