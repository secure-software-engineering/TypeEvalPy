# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [85, 94, 46]


def func2():
    return {'mltse': 68, 'nnvom': 32, 'inljb': 37}


def func3():
    return 14


def func4():
    return (96, 87, 2)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
