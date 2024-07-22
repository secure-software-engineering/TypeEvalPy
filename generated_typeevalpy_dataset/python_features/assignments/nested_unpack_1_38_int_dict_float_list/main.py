# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 58


def func2():
    return {'hnckz': 22, 'jlnmc': 6, 'poswy': 73}


def func3():
    return 75.15


def func4():
    return [12, 96, 49]


(a, b), (c, d) = [(func1, func2), (func3, func4)]