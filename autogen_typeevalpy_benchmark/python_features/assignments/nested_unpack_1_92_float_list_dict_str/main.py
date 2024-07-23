# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1.28


def func2():
    return [84, 82, 93]


def func3():
    return {'bdmhf': 38, 'lcyys': 2, 'mjaff': 12}


def func4():
    return 'lumgr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
