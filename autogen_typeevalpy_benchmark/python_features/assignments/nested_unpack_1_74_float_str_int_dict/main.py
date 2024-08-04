# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 9.48


def func2():
    return 'zbnnz'


def func3():
    return 71


def func4():
    return {'awbkj': 44, 'tjbgr': 83, 'cptdj': 23}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
