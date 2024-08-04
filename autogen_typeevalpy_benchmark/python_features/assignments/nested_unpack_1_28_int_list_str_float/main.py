# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 23


def func2():
    return [39, 2, 91]


def func3():
    return 'nhzos'


def func4():
    return 13.5


(a, b), (c, d) = [(func1, func2), (func3, func4)]
