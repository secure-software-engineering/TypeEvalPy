# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'pxnal': 73, 'xoijz': 34, 'hesph': 8}


def func2():
    return [81, 61, 75]


def func3():
    return 17.74


def func4():
    return (7, 85, 38)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
