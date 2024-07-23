# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (66, 21, 48)


def func2():
    return [53, 8, 16]


def func3():
    return 57.4


def func4():
    return 'epvml'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
