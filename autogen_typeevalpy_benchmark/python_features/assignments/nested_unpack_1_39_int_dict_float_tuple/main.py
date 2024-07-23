# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 58


def func2():
    return {'loesw': 32, 'vknaw': 70, 'struo': 4}


def func3():
    return 58.6


def func4():
    return (30, 35, 38)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
