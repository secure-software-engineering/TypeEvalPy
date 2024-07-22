# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 53


def func2():
    return 'nnmos'


def func3():
    return (87, 34, 63)


def func4():
    return [98, 4, 20]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
