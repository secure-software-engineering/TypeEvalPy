# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 33.43


def func2():
    return {'gtnoc': 68, 'rghxp': 13, 'rbxnp': 27}


def func3():
    return 34


def func4():
    return 'seskr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
