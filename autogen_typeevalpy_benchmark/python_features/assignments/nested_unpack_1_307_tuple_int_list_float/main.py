# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (22, 47, 86)


def func2():
    return 85


def func3():
    return [40, 42, 54]


def func4():
    return 79.1


(a, b), (c, d) = [(func1, func2), (func3, func4)]
