# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (37, 24, 22)


def func2():
    return {'tvorf': 88, 'zatex': 16, 'gmcih': 51}


def func3():
    return 37.98


def func4():
    return 'ycial'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
