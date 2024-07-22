# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ivzvv': 96, 'zqsph': 13, 'ycdbv': 54}


def func2():
    return (61, 27, 51)


def func3():
    return 77


def func4():
    return 'sxgho'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
