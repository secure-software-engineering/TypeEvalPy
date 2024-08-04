# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'yrgsx': 89, 'onyml': 100, 'vuuoa': 62}


def func2():
    return (16, 73, 69)


def func3():
    return 46


def func4():
    return 34.01


(a, b), (c, d) = [(func1, func2), (func3, func4)]
