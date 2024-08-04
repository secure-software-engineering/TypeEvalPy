# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'qjtxv': 30, 'ubqnt': 69, 'vcfnc': 50}


def func2():
    return 25


def func3():
    return [25, 68, 85]


def func4():
    return 'gqetk'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
