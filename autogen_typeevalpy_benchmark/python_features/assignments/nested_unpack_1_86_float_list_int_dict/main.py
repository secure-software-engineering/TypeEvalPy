# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 98.3


def func2():
    return [81, 40, 83]


def func3():
    return 71


def func4():
    return {'qvpxv': 97, 'iwovf': 74, 'pplnu': 66}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
