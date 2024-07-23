# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'bghfe'


def func2():
    return {'vrzdt': 80, 'rxzkp': 72, 'ifqbu': 34}


def func3():
    return 52.8


def func4():
    return 67


(a, b), (c, d) = [(func1, func2), (func3, func4)]
