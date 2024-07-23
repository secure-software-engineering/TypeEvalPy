# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 33


def func2():
    return 'aajlg'


def func3():
    return {'rmrer': 3, 'ubnyu': 2, 'xtpwq': 29}


def func4():
    return [54, 19, 59]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
