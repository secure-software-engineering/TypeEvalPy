# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (29, 38, 15)


def func2():
    return {'egwfk': 64, 'rrdnw': 4, 'irybv': 62}


def func3():
    return 44.32


def func4():
    return [64, 6, 91]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
