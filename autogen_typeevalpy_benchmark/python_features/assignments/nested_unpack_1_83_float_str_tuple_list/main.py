# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1.63


def func2():
    return 'hwyvf'


def func3():
    return (68, 52, 14)


def func4():
    return [78, 31, 50]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
