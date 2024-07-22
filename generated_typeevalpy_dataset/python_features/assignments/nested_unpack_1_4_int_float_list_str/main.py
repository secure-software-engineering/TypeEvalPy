# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 81


def func2():
    return 97.87


def func3():
    return [30, 59, 80]


def func4():
    return 'jdsxm'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
