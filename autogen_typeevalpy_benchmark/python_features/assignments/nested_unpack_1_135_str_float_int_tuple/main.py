# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'uonpe'


def func2():
    return 97.92


def func3():
    return 38


def func4():
    return (38, 74, 35)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
