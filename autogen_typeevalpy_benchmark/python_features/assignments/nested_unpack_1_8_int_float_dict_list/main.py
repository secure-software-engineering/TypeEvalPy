# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 95


def func2():
    return 81.26


def func3():
    return {'gucww': 99, 'fvlhu': 36, 'fafiw': 45}


def func4():
    return [83, 66, 52]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
