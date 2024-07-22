# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'smrbm': 38, 'icnok': 56, 'eyriq': 78}


def func2():
    return 'ycfme'


def func3():
    return [5, 74, 54]


def func4():
    return 27.53


(a, b), (c, d) = [(func1, func2), (func3, func4)]
