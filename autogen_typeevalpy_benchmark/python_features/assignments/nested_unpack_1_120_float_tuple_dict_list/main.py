# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 26.91


def func2():
    return (18, 11, 60)


def func3():
    return {'mjgjq': 72, 'injmt': 1, 'wjsbk': 20}


def func4():
    return [79, 20, 89]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
