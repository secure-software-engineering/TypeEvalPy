# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48.23


def func2():
    return {'fpmlp': 70, 'ioawl': 67, 'faubp': 58}


def func3():
    return [67, 63, 18]


def func4():
    return 'vfolk'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
