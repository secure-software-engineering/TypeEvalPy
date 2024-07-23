# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [62, 96, 13]


def func2():
    return (99, 4, 59)


def func3():
    return 22


def func4():
    return 'oajmb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
