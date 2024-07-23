# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [4, 12, 90]


def func2():
    return {'pfesk': 66, 'bdjgz': 11, 'wcaqh': 68}


def func3():
    return (13, 47, 49)


def func4():
    return 29


(a, b), (c, d) = [(func1, func2), (func3, func4)]
