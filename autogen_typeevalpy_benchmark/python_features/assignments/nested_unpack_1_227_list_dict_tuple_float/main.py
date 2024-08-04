# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [29, 87, 90]


def func2():
    return {'fiyna': 35, 'vgcrv': 24, 'bymjx': 96}


def func3():
    return (88, 25, 64)


def func4():
    return 73.97


(a, b), (c, d) = [(func1, func2), (func3, func4)]
