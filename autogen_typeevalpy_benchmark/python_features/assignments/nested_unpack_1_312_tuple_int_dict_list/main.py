# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (89, 38, 54)


def func2():
    return 93


def func3():
    return {'nuhhk': 72, 'gvfda': 28, 'mmbdf': 29}


def func4():
    return [66, 13, 2]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
