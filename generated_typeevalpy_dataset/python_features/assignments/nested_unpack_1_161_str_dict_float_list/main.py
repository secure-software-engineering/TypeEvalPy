# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'wdrhu'


def func2():
    return {'yeasy': 96, 'wvcfk': 95, 'wklwo': 85}


def func3():
    return 87.19


def func4():
    return [28, 57, 73]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
