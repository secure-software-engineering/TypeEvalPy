# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ztjat': 53, 'ixvtv': 68, 'bmdwi': 27}


def func2():
    return 'spcsq'


def func3():
    return 12


def func4():
    return (62, 93, 89)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
