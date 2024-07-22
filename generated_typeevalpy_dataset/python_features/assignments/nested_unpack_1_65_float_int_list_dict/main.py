# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 26.92


def func2():
    return 90


def func3():
    return [48, 21, 82]


def func4():
    return {'vsuwr': 87, 'xnyby': 77, 'clclb': 44}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
