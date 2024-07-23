# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (88, 44, 4)


def func2():
    return 57.5


def func3():
    return {'cepzc': 57, 'fwxsm': 90, 'zjitw': 4}


def func4():
    return 'gwjgq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
