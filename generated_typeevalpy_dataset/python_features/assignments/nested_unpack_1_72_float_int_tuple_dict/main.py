# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 80.0


def func2():
    return 23


def func3():
    return (31, 63, 75)


def func4():
    return {'yqwva': 11, 'pjtge': 31, 'ihbtz': 94}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
