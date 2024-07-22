# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 24


def func2():
    return [86, 21, 23]


def func3():
    return {'qxlmq': 98, 'iffdl': 97, 'owqud': 20}


def func4():
    return 'mkqdr'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
