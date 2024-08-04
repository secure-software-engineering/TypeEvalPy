# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 64.14


def func2():
    return (79, 62, 85)


def func3():
    return 'maoan'


def func4():
    return {'hzavr': 48, 'uxccd': 52, 'envgk': 59}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
