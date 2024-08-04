# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 45


def func2():
    return (1, 24, 19)


def func3():
    return [73, 85, 52]


def func4():
    return 7.89


(a, b), (c, d) = [(func1, func2), (func3, func4)]
