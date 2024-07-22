# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'hygra': 55, 'zfqvv': 62, 'xakfb': 61}


def func2():
    return (3, 33, 90)


def func3():
    return 'ritzq'


def func4():
    return 77


(a, b), (c, d) = [(func1, func2), (func3, func4)]
