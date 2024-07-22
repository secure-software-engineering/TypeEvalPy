# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31


def func2():
    return (93, 50, 87)


def func3():
    return 'daxyo'


def func4():
    return [61, 100, 58]


(a, b), (c, d) = [(func1, func2), (func3, func4)]