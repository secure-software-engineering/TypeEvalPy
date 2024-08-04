# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [49, 15, 50]


def func2():
    return 'gsanu'


def func3():
    return 66


def func4():
    return {'ulbxf': 55, 'nyeyn': 14, 'abruw': 27}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
