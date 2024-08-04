# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'kqefv'


def func2():
    return (95, 63, 98)


def func3():
    return 67


def func4():
    return 86.85


(a, b), (c, d) = [(func1, func2), (func3, func4)]
