# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'gnorf'


def func2():
    return {'ujnws': 9, 'dbflw': 11, 'qnzdj': 98}


def func3():
    return [38, 8, 82]


def func4():
    return 61


(a, b), (c, d) = [(func1, func2), (func3, func4)]
