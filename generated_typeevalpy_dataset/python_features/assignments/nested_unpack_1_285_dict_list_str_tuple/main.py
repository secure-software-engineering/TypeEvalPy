# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'jzlnb': 66, 'zqcgr': 88, 'dkuxg': 5}


def func2():
    return [34, 59, 100]


def func3():
    return 'hxpfz'


def func4():
    return (67, 69, 48)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
