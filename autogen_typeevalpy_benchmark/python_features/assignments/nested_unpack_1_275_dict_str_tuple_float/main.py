# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'mgfwq': 60, 'xksru': 22, 'wlamj': 37}


def func2():
    return 'tpdcv'


def func3():
    return (14, 42, 72)


def func4():
    return 65.3


(a, b), (c, d) = [(func1, func2), (func3, func4)]
