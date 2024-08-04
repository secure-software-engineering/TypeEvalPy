# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 27


def func2():
    return 72.04


def func3():
    return [27, 88, 82]


def func4():
    return {'wngxb': 15, 'qvbid': 10, 'zelso': 89}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
