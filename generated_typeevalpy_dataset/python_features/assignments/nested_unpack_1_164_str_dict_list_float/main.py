# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'jslqo'


def func2():
    return {'keund': 82, 'ueqkg': 53, 'ytdga': 70}


def func3():
    return [10, 2, 3]


def func4():
    return 83.76


(a, b), (c, d) = [(func1, func2), (func3, func4)]
