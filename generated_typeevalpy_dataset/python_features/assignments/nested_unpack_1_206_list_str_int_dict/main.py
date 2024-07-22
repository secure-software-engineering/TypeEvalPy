# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [48, 71, 32]


def func2():
    return 'whngw'


def func3():
    return 100


def func4():
    return {'glshv': 81, 'haile': 66, 'wbqbc': 93}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
