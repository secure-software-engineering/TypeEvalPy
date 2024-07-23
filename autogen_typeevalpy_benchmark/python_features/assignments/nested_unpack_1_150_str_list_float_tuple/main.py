# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'ludcv'


def func2():
    return [88, 27, 23]


def func3():
    return 84.02


def func4():
    return (7, 43, 22)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
