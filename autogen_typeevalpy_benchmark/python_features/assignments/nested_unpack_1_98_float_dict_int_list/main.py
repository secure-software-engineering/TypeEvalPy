# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 88.18


def func2():
    return {'mqthh': 5, 'btqgt': 51, 'waxkv': 64}


def func3():
    return 24


def func4():
    return [96, 38, 5]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
