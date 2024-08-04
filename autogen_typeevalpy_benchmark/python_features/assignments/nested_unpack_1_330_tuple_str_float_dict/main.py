# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (23, 49, 78)


def func2():
    return 'rdqcb'


def func3():
    return 75.41


def func4():
    return {'tufrm': 49, 'giwoy': 57, 'alxji': 59}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
