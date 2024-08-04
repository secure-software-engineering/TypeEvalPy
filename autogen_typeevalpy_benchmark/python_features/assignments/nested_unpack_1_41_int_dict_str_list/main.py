# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 88


def func2():
    return {'uecwq': 21, 'gxdlg': 10, 'gauxr': 57}


def func3():
    return 'yzhzr'


def func4():
    return [59, 39, 26]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
