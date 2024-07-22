# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'smvaf': 62, 'jezir': 58, 'fmrsb': 79}


def func2():
    return 73


def func3():
    return 'pyndt'


def func4():
    return [4, 70, 42]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
