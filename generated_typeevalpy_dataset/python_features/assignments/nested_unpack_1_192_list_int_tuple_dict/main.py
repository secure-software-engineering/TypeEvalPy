# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [82, 16, 26]


def func2():
    return 69


def func3():
    return (37, 12, 24)


def func4():
    return {'zpgef': 25, 'mhsrx': 49, 'dwmtd': 77}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
