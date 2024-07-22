# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 53.63


def func2():
    return 77


def func3():
    return 'gvrga'


def func4():
    return [32, 4, 48]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
