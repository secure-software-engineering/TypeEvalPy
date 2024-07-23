# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'fdcpf'


def func2():
    return 44


def func3():
    return {'pbdok': 37, 'qrjxq': 97, 'cjudy': 8}


def func4():
    return 59.27


(a, b), (c, d) = [(func1, func2), (func3, func4)]
