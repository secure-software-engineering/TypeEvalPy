# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1


def func2():
    return (27, 39, 28)


def func3():
    return {'tthdm': 59, 'ldnfo': 10, 'rjktl': 41}


def func4():
    return 58.0


(a, b), (c, d) = [(func1, func2), (func3, func4)]
