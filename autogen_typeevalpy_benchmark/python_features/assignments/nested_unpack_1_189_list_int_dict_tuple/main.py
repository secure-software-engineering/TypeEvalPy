# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [83, 11, 57]


def func2():
    return 67


def func3():
    return {'jzrgd': 77, 'wgmfm': 25, 'ardja': 24}


def func4():
    return (31, 23, 8)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
