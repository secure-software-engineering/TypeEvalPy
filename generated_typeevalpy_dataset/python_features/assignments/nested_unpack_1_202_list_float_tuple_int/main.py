# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [53, 30, 9]


def func2():
    return 68.2


def func3():
    return (55, 83, 8)


def func4():
    return 82


(a, b), (c, d) = [(func1, func2), (func3, func4)]