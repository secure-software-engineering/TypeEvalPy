# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'svqky': 19, 'qjnqm': 61, 'ducdo': 34}


def func2():
    return [37, 90, 98]


def func3():
    return 'pghvr'


def func4():
    return 96


(a, b), (c, d) = [(func1, func2), (func3, func4)]