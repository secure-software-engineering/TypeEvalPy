# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'uvfmx'


def func2():
    return (46, 73, 88)


def func3():
    return {'uwgdd': 94, 'hdtfr': 71, 'vqxov': 37}


def func4():
    return 49.1


(a, b), (c, d) = [(func1, func2), (func3, func4)]
