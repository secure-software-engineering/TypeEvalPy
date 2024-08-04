# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [10, 38, 86]


def func2():
    return 'bcsmi'


def func3():
    return {'drcqx': 32, 'ilqhp': 29, 'ojila': 92}


def func4():
    return 74.24


(a, b), (c, d) = [(func1, func2), (func3, func4)]
