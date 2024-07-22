# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'kfika': 54, 'hbyof': 36, 'gxywb': 97}


def func2():
    return 71


def func3():
    return (59, 33, 57)


def func4():
    return 'zhhpm'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
