# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 49


def func2():
    return 'fwaiz'


def func3():
    return 79.29


def func4():
    return [1, 95, 29]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
