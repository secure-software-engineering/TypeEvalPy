# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (5, 5, 23)


def func2():
    return 'owhsm'


def func3():
    return [18, 40, 92]


def func4():
    return 50


(a, b), (c, d) = [(func1, func2), (func3, func4)]
