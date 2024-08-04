# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (21, 75, 8)


def func2():
    return 15.47


def func3():
    return 'lsjbj'


def func4():
    return {'qybhq': 35, 'bfqtp': 88, 'eiivu': 90}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
