# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 75.67


def func2():
    return 'xiqiv'


def func3():
    return {'gqwwg': 27, 'ybopd': 81, 'zarkf': 24}


def func4():
    return [56, 59, 84]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
