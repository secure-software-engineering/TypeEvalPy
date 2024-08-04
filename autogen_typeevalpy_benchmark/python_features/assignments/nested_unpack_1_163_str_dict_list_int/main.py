# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'qrebv'


def func2():
    return {'hiybe': 22, 'jtoxc': 78, 'ppmay': 56}


def func3():
    return [21, 7, 13]


def func4():
    return 43


(a, b), (c, d) = [(func1, func2), (func3, func4)]
