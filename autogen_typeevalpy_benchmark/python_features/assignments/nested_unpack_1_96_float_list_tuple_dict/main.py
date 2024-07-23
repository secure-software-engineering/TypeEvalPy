# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 88.28


def func2():
    return [57, 76, 21]


def func3():
    return (14, 8, 40)


def func4():
    return {'juvla': 49, 'idbsq': 50, 'scywc': 81}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
