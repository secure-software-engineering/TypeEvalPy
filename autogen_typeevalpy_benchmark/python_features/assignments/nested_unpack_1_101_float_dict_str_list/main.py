# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 31.37


def func2():
    return {'knxsi': 71, 'dxhpf': 61, 'ddtpk': 97}


def func3():
    return 'nrfgt'


def func4():
    return [11, 68, 58]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
