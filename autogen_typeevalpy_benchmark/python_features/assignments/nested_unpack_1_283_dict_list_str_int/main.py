# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'fkcol': 30, 'ddvmh': 51, 'hmgdb': 90}


def func2():
    return [59, 93, 86]


def func3():
    return 'koeaa'


def func4():
    return 97


(a, b), (c, d) = [(func1, func2), (func3, func4)]
