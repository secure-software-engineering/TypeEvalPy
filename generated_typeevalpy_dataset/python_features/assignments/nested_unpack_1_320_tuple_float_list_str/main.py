# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (40, 9, 8)


def func2():
    return 72.27


def func3():
    return [86, 2, 73]


def func4():
    return 'ayaug'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
