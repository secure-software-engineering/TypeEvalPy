# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (32, 67, 55)


def func2():
    return {'hbbbc': 23, 'lcrog': 24, 'gcncr': 51}


def func3():
    return 'bksis'


def func4():
    return [97, 86, 58]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
