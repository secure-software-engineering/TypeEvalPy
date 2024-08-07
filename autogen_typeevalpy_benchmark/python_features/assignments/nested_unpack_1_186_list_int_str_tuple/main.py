# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [41, 55, 95]


def func2():
    return 15


def func3():
    return 'ctbwr'


def func4():
    return (22, 43, 46)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
