# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 23.75


def func2():
    return 14


def func3():
    return 'qgnbt'


def func4():
    return {'ydmle': 24, 'xouok': 73, 'jvzyo': 52}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
