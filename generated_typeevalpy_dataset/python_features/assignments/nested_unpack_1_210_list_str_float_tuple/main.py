# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [67, 18, 52]


def func2():
    return 'dzbxu'


def func3():
    return 82.57


def func4():
    return (8, 100, 41)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
