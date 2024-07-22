# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 1.16


def func2():
    return 'afurd'


def func3():
    return [90, 77, 58]


def func4():
    return (76, 42, 76)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
