# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (88, 62, 56)


def func2():
    return 2.08


def func3():
    return 74


def func4():
    return {'czjlu': 90, 'pmcbu': 93, 'osjgc': 11}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
