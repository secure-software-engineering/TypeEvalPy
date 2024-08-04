# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (29, 17, 89)


def func2():
    return 15.09


def func3():
    return {'fddcr': 33, 'ucutb': 6, 'cunbd': 9}


def func4():
    return 39


(a, b), (c, d) = [(func1, func2), (func3, func4)]
