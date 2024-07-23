# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jzncz': 26, 'mbkaw': 72, 'uaggu': 60}


def func2():
    return 81


def func3():
    return (62, 47, 82)


def func4():
    return [96, 1, 5]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
