# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (97, 83, 52)


def func2():
    return 'jryzn'


def func3():
    return 15.59


def func4():
    return 59


(a, b), (c, d) = [(func1, func2), (func3, func4)]
