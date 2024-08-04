# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'eybcv': 19, 'ujmrc': 85, 'vxxqa': 20}


def func2():
    return [58, 69, 38]


def func3():
    return 50


def func4():
    return 61.94


(a, b), (c, d) = [(func1, func2), (func3, func4)]
