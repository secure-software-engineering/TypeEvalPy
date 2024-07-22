# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 50


def func2():
    return {'dmyzt': 62, 'lhqus': 90, 'nruom': 48}


def func3():
    return 10.37


def func4():
    return 'puzoa'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
