# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 65.22


def func2():
    return (40, 34, 47)


def func3():
    return 66


def func4():
    return 'wmust'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
