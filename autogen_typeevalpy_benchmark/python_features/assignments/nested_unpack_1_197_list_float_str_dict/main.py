# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [7, 76, 62]


def func2():
    return 74.37


def func3():
    return 'vngvw'


def func4():
    return {'tvaxw': 19, 'iicra': 10, 'zgbso': 37}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
