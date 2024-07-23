# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ehvyi': 70, 'ffohl': 15, 'zeges': 88}


def func2():
    return 'likco'


def func3():
    return 81


def func4():
    return (65, 45, 26)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
