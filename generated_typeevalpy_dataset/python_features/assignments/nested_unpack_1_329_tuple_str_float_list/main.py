# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (51, 98, 52)


def func2():
    return 'mzhzi'


def func3():
    return 99.64


def func4():
    return [29, 65, 100]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
