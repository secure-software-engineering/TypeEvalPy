# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 19.11


def func2():
    return 'cipap'


def func3():
    return {'nwupn': 73, 'metxd': 94, 'qalrj': 80}


def func4():
    return (31, 86, 12)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
