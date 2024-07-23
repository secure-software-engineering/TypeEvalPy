# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'zszce': 32, 'ywvpm': 41, 'bxcsm': 24}


def func2():
    return 6


def func3():
    return (27, 92, 48)


def func4():
    return 6.59


(a, b), (c, d) = [(func1, func2), (func3, func4)]
