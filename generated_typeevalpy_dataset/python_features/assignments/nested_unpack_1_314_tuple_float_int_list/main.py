# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (20, 83, 20)


def func2():
    return 7.92


def func3():
    return 16


def func4():
    return [19, 84, 2]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
