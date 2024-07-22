# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'anifi': 96, 'psmdw': 73, 'fkxvd': 28}


def func2():
    return [46, 100, 70]


def func3():
    return 71


def func4():
    return 89.42


(a, b), (c, d) = [(func1, func2), (func3, func4)]
