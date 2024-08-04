# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (91, 9, 72)


def func2():
    return 91


def func3():
    return 77.58


def func4():
    return {'dioqt': 48, 'twstt': 45, 'ixnkb': 58}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
