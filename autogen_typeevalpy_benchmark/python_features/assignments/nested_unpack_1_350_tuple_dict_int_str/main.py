# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (77, 33, 10)


def func2():
    return {'cbigx': 48, 'zyzpt': 17, 'bgqhk': 72}


def func3():
    return 6


def func4():
    return 'pgnyw'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
