# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 12


def func2():
    return 12.0


def func3():
    return {'voowq': 36, 'jxwkg': 68, 'ooucr': 75}


def func4():
    return [95, 39, 65]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
