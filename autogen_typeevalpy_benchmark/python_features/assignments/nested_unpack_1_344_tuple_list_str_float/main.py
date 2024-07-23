# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (88, 39, 100)


def func2():
    return [27, 18, 56]


def func3():
    return 'xbdve'


def func4():
    return 3.96


(a, b), (c, d) = [(func1, func2), (func3, func4)]
