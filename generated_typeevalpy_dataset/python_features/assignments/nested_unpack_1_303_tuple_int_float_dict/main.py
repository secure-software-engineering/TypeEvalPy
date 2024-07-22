# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (32, 29, 52)


def func2():
    return 33


def func3():
    return 68.36


def func4():
    return {'pavrp': 100, 'gttaa': 32, 'wmnws': 48}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
