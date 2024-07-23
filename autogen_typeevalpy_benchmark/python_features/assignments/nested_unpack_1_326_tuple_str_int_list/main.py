# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (57, 26, 31)


def func2():
    return 'hblhp'


def func3():
    return 72


def func4():
    return [98, 59, 44]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
