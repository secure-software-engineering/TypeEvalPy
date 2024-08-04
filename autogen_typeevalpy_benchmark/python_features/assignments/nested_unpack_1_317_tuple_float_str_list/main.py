# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (62, 73, 56)


def func2():
    return 86.97


def func3():
    return 'qmsdn'


def func4():
    return [74, 3, 34]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
