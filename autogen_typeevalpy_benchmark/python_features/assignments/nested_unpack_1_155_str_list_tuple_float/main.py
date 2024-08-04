# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'veywo'


def func2():
    return [71, 32, 13]


def func3():
    return (60, 14, 18)


def func4():
    return 13.02


(a, b), (c, d) = [(func1, func2), (func3, func4)]
