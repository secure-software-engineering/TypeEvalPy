# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ixwfc'


def func2():
    return 60


def func3():
    return 12.15


def func4():
    return (71, 65, 77)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
