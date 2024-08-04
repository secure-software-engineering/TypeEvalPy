# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'gsxhd'


def func2():
    return (98, 31, 8)


def func3():
    return [77, 52, 85]


def func4():
    return 41


(a, b), (c, d) = [(func1, func2), (func3, func4)]
