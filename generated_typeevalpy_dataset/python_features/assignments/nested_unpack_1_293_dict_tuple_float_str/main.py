# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'berjj': 17, 'fdhgp': 96, 'qvouf': 86}


def func2():
    return (11, 26, 99)


def func3():
    return 4.96


def func4():
    return 'uvnam'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
