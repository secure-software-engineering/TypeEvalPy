# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (1, 19, 37)


def func2():
    return [69, 39, 44]


def func3():
    return 'cqmwa'


def func4():
    return {'uvfqt': 26, 'qxjgg': 73, 'tbrwo': 10}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
