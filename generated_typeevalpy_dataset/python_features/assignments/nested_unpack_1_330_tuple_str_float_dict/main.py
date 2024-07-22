# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (10, 41, 1)


def func2():
    return 'nohvt'


def func3():
    return 93.15


def func4():
    return {'twaod': 51, 'qntpg': 26, 'ltjou': 55}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
