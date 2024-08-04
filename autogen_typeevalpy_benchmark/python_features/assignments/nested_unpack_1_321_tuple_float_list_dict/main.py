# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (79, 89, 68)


def func2():
    return 84.76


def func3():
    return [92, 71, 90]


def func4():
    return {'tclbv': 4, 'ymijv': 96, 'xptis': 16}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
