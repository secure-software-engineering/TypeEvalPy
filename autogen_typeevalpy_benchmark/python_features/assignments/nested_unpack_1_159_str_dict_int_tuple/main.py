# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'eqjyu'


def func2():
    return {'eoybl': 22, 'ftabz': 61, 'zshlh': 73}


def func3():
    return 91


def func4():
    return (67, 51, 95)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
