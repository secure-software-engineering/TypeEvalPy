# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 38


def func2():
    return {'ticzd': 59, 'zwszz': 48, 'ujuan': 87}


def func3():
    return [96, 87, 34]


def func4():
    return 'pvycg'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
