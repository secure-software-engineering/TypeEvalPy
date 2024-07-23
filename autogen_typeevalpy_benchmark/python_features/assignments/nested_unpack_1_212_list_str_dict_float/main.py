# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [81, 8, 59]


def func2():
    return 'gdzhv'


def func3():
    return {'zijwc': 99, 'lwqnm': 25, 'qxdej': 93}


def func4():
    return 37.59


(a, b), (c, d) = [(func1, func2), (func3, func4)]
