# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 27.91


def func2():
    return 6


def func3():
    return {'zsepg': 13, 'abytg': 69, 'nsvzc': 22}


def func4():
    return 'sdzzp'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
