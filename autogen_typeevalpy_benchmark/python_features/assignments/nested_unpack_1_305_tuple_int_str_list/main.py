# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (64, 23, 34)


def func2():
    return 45


def func3():
    return 'bzjfn'


def func4():
    return [91, 10, 57]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
