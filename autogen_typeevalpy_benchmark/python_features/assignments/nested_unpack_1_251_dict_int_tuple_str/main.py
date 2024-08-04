# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'noocl': 42, 'egxgg': 62, 'hoofc': 23}


def func2():
    return 63


def func3():
    return (89, 90, 74)


def func4():
    return 'vcqav'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
