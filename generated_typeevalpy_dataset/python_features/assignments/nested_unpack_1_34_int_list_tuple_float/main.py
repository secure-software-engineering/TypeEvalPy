# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 72


def func2():
    return [35, 9, 18]


def func3():
    return (9, 81, 73)


def func4():
    return 65.4


(a, b), (c, d) = [(func1, func2), (func3, func4)]
