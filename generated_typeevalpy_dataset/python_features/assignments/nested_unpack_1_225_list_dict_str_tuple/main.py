# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [94, 31, 94]


def func2():
    return {'ykamg': 98, 'esgou': 86, 'xrpqd': 48}


def func3():
    return 'ssone'


def func4():
    return (96, 68, 73)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
