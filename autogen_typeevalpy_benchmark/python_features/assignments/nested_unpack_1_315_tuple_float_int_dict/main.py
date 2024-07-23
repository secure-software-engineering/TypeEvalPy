# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (46, 23, 21)


def func2():
    return 25.22


def func3():
    return 33


def func4():
    return {'lvwbz': 97, 'drgal': 83, 'zqnam': 38}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
