# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [51, 88, 100]


def func2():
    return (23, 59, 16)


def func3():
    return 90


def func4():
    return 'niarj'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
