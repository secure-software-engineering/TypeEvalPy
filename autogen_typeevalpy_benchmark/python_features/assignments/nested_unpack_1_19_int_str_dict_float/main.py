# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 70


def func2():
    return 'uxmhm'


def func3():
    return {'krusv': 34, 'xznxp': 49, 'rclwe': 42}


def func4():
    return 21.95


(a, b), (c, d) = [(func1, func2), (func3, func4)]
