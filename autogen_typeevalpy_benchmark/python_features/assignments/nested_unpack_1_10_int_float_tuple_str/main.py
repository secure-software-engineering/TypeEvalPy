# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 69


def func2():
    return 69.0


def func3():
    return (95, 95, 86)


def func4():
    return 'flyxq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
