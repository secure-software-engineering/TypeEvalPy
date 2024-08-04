# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'pfwds'


def func2():
    return [46, 51, 66]


def func3():
    return (7, 87, 39)


def func4():
    return 34


(a, b), (c, d) = [(func1, func2), (func3, func4)]
