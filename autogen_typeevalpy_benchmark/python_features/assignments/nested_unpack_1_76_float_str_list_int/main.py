# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 30.05


def func2():
    return 'bfbyn'


def func3():
    return [70, 61, 33]


def func4():
    return 5


(a, b), (c, d) = [(func1, func2), (func3, func4)]
