# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'rlxfn': 40, 'kiimq': 17, 'tpoij': 95}


def func2():
    return [3, 42, 20]


def func3():
    return 24


def func4():
    return 'opvyz'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
