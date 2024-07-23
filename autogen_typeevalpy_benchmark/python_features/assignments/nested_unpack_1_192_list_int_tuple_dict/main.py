# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [71, 39, 48]


def func2():
    return 95


def func3():
    return (42, 62, 43)


def func4():
    return {'aserr': 7, 'vougb': 97, 'znjss': 83}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
