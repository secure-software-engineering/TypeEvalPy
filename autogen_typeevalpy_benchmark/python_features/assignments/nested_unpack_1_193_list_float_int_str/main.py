# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [92, 58, 15]


def func2():
    return 10.65


def func3():
    return 85


def func4():
    return 'fivzh'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
