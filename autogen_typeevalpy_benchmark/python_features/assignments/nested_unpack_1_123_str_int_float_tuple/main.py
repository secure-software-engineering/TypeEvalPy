# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'zuihu'


def func2():
    return 47


def func3():
    return 12.27


def func4():
    return (73, 26, 76)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
