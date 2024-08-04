# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (17, 12, 41)


def func2():
    return {'slgiz': 56, 'mzhjl': 22, 'xgvyn': 41}


def func3():
    return 95


def func4():
    return [63, 98, 20]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
