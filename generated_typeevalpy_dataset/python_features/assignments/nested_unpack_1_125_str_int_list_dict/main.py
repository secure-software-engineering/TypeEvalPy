# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'chuda'


def func2():
    return 64


def func3():
    return [41, 38, 22]


def func4():
    return {'efpoj': 36, 'fbdrg': 8, 'ilkjy': 53}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
