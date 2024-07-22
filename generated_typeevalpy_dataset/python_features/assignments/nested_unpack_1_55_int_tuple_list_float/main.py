# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 20


def func2():
    return (2, 7, 56)


def func3():
    return [63, 25, 3]


def func4():
    return 59.65


(a, b), (c, d) = [(func1, func2), (func3, func4)]
