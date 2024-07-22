# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 6


def func2():
    return {'ymauf': 39, 'apoya': 5, 'efprc': 2}


def func3():
    return 12.61


def func4():
    return (28, 75, 12)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
