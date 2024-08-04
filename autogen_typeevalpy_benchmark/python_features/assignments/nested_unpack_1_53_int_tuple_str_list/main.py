# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 72


def func2():
    return (43, 86, 16)


def func3():
    return 'kwykx'


def func4():
    return [7, 37, 77]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
