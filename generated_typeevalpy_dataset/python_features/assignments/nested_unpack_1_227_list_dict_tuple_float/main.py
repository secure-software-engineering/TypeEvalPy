# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [33, 21, 64]


def func2():
    return {'mioez': 38, 'inwvp': 14, 'rjlgq': 48}


def func3():
    return (49, 50, 26)


def func4():
    return 55.45


(a, b), (c, d) = [(func1, func2), (func3, func4)]
