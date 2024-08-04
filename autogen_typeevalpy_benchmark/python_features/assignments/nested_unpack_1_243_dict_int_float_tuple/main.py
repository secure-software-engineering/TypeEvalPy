# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'talun': 82, 'zmrii': 39, 'qbyng': 26}


def func2():
    return 47


def func3():
    return 88.86


def func4():
    return (86, 28, 15)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
