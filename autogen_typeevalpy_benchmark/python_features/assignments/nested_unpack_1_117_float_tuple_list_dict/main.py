# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 78.65


def func2():
    return (73, 13, 68)


def func3():
    return [6, 30, 28]


def func4():
    return {'xrohy': 51, 'rhore': 10, 'wafdv': 39}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
