# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'mlsih'


def func2():
    return 91


def func3():
    return {'cwqre': 56, 'zgeeo': 51, 'ygkeq': 4}


def func4():
    return [95, 79, 26]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
