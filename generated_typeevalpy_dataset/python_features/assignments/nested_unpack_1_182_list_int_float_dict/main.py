# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [62, 77, 6]


def func2():
    return 41


def func3():
    return 14.44


def func4():
    return {'sljcy': 10, 'ryxji': 78, 'wpljm': 20}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
