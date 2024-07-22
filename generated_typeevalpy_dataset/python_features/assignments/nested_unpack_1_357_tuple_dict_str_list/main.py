# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (89, 73, 67)


def func2():
    return {'menpf': 11, 'keqbr': 7, 'wgfgr': 55}


def func3():
    return 'aoljs'


def func4():
    return [18, 25, 36]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
