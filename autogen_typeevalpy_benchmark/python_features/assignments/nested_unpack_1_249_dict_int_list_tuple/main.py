# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'cqjlr': 42, 'weeki': 48, 'ezlji': 53}


def func2():
    return 98


def func3():
    return [82, 56, 93]


def func4():
    return (42, 78, 31)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
