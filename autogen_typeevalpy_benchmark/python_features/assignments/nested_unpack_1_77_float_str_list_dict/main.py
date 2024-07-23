# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 68.97


def func2():
    return 'hxcsj'


def func3():
    return [58, 44, 7]


def func4():
    return {'xjloi': 37, 'qrhjd': 91, 'eplcr': 75}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
