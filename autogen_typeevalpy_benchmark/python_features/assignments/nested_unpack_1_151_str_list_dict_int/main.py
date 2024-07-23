# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'tejes'


def func2():
    return [7, 58, 34]


def func3():
    return {'itcgz': 71, 'zsedw': 19, 'hjywk': 92}


def func4():
    return 59


(a, b), (c, d) = [(func1, func2), (func3, func4)]
