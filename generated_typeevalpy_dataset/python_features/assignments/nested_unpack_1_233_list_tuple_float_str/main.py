# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [4, 96, 72]


def func2():
    return (63, 51, 43)


def func3():
    return 55.3


def func4():
    return 'elszj'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
