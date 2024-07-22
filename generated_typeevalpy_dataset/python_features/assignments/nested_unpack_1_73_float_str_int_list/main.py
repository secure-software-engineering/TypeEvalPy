# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 37.21


def func2():
    return 'hxjgl'


def func3():
    return 30


def func4():
    return [65, 84, 3]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
