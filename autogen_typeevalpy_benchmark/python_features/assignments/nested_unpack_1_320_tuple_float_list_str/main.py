# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (67, 37, 48)


def func2():
    return 78.1


def func3():
    return [53, 44, 21]


def func4():
    return 'cefex'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
