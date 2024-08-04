# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (97, 69, 1)


def func2():
    return 97.38


def func3():
    return {'cfnsj': 16, 'plyej': 60, 'jffcz': 15}


def func4():
    return [67, 18, 64]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
