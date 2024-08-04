# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'rsrzg'


def func2():
    return (54, 52, 50)


def func3():
    return [95, 5, 75]


def func4():
    return 71.1


(a, b), (c, d) = [(func1, func2), (func3, func4)]
