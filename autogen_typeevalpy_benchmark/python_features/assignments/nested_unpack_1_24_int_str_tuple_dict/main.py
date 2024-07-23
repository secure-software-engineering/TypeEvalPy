# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 53


def func2():
    return 'yflaa'


def func3():
    return (96, 36, 8)


def func4():
    return {'swahp': 70, 'xpnvg': 21, 'dmwtq': 70}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
