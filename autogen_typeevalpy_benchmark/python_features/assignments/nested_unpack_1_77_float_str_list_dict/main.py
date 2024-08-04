# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 75.58


def func2():
    return 'ejuwi'


def func3():
    return [16, 48, 56]


def func4():
    return {'xtxkz': 42, 'mmynu': 14, 'scpvo': 11}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
