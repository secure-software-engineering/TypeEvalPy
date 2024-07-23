# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 93.88


def func2():
    return [96, 21, 92]


def func3():
    return (45, 5, 77)


def func4():
    return 38


(a, b), (c, d) = [(func1, func2), (func3, func4)]
