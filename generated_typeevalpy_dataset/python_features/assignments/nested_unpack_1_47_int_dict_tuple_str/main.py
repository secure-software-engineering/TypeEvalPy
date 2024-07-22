# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 82


def func2():
    return {'nnovz': 62, 'bqush': 43, 'imynb': 63}


def func3():
    return (60, 2, 34)


def func4():
    return 'zwlad'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
