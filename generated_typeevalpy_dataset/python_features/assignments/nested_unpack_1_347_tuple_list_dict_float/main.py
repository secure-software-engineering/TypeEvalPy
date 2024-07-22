# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (69, 5, 55)


def func2():
    return [15, 14, 44]


def func3():
    return {'vxzod': 74, 'afogl': 11, 'sbybd': 59}


def func4():
    return 95.48


(a, b), (c, d) = [(func1, func2), (func3, func4)]
