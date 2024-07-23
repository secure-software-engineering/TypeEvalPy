# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (4, 34, 8)


def func2():
    return [8, 5, 29]


def func3():
    return 21


def func4():
    return 'lhxfn'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
