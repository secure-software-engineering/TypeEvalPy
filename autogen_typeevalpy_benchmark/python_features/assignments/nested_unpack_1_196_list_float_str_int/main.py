# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [21, 74, 82]


def func2():
    return 46.43


def func3():
    return 'pkcjo'


def func4():
    return 92


(a, b), (c, d) = [(func1, func2), (func3, func4)]
