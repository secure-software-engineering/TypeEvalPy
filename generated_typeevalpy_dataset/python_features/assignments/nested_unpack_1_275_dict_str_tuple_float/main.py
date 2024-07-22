# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'natos': 15, 'ipyqy': 94, 'kbmis': 46}


def func2():
    return 'yhqmc'


def func3():
    return (31, 86, 57)


def func4():
    return 63.31


(a, b), (c, d) = [(func1, func2), (func3, func4)]
