# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jbjyv': 59, 'phegp': 85, 'vkrdo': 50}


def func2():
    return 'eacqt'


def func3():
    return (37, 40, 52)


def func4():
    return [57, 38, 56]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
