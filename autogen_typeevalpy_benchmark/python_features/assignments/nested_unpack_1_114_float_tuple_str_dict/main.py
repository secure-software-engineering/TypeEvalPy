# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 65.99


def func2():
    return (5, 52, 52)


def func3():
    return 'ncayb'


def func4():
    return {'abbgj': 6, 'qomhx': 16, 'dthmu': 29}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
