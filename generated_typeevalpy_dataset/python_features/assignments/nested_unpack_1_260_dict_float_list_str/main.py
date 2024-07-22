# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'abrkg': 84, 'jyvdg': 13, 'yevzu': 45}


def func2():
    return 76.2


def func3():
    return [8, 85, 6]


def func4():
    return 'xeuje'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
