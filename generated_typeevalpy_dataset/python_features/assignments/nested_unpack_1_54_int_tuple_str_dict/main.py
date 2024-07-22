# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48


def func2():
    return (70, 61, 83)


def func3():
    return 'kkzod'


def func4():
    return {'vrjmi': 37, 'zykxi': 14, 'zpgti': 83}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
