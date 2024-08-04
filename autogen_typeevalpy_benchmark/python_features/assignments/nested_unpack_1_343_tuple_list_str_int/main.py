# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (47, 61, 92)


def func2():
    return [48, 40, 3]


def func3():
    return 'qxatu'


def func4():
    return 7


(a, b), (c, d) = [(func1, func2), (func3, func4)]
