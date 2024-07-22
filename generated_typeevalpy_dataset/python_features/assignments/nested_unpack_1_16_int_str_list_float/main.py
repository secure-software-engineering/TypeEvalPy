# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 36


def func2():
    return 'cvdnp'


def func3():
    return [49, 34, 10]


def func4():
    return 87.19


(a, b), (c, d) = [(func1, func2), (func3, func4)]
