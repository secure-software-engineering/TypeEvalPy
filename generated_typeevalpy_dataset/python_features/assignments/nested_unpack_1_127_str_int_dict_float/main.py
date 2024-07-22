# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'xojbj'


def func2():
    return 90


def func3():
    return {'qknwv': 74, 'ybwkm': 90, 'ejryq': 19}


def func4():
    return 37.67


(a, b), (c, d) = [(func1, func2), (func3, func4)]
