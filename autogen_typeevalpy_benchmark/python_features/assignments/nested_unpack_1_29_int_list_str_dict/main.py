# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 97


def func2():
    return [63, 14, 2]


def func3():
    return 'omleb'


def func4():
    return {'ymvkb': 29, 'qbdoh': 100, 'zdtpu': 67}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
