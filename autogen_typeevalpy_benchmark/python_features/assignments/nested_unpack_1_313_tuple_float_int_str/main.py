# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (12, 19, 27)


def func2():
    return 31.02


def func3():
    return 68


def func4():
    return 'zbytc'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
