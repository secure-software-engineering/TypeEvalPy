# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'puslw': 30, 'goqyp': 91, 'msmvw': 38}


def func2():
    return 'zaaqd'


def func3():
    return 84.96


def func4():
    return 79


(a, b), (c, d) = [(func1, func2), (func3, func4)]
