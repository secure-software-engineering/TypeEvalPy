# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [63, 27, 90]


def func2():
    return 61


def func3():
    return 'qqmns'


def func4():
    return (87, 17, 74)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
