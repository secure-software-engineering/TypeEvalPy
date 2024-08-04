# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [91, 96, 1]


def func2():
    return {'pdarr': 97, 'ijeqg': 27, 'wljhr': 53}


def func3():
    return 55.66


def func4():
    return (72, 62, 23)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
