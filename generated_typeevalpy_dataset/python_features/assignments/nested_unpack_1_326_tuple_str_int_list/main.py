# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (77, 68, 4)


def func2():
    return 'bxpyc'


def func3():
    return 97


def func4():
    return [51, 89, 97]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
