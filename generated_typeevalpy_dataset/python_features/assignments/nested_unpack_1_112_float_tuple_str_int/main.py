# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 94.15


def func2():
    return (55, 73, 35)


def func3():
    return 'hidmq'


def func4():
    return 71


(a, b), (c, d) = [(func1, func2), (func3, func4)]
