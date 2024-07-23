# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 13.05


def func2():
    return {'ncbpv': 8, 'uigpt': 13, 'kbjyt': 47}


def func3():
    return 'ekzop'


def func4():
    return (57, 57, 68)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
