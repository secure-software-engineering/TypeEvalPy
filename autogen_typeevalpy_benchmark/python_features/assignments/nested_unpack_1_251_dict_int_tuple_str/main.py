# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'pcaxi': 31, 'vlwjb': 27, 'spdez': 7}


def func2():
    return 67


def func3():
    return (82, 24, 83)


def func4():
    return 'gmgti'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
