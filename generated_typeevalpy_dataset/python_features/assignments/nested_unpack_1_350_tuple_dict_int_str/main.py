# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (4, 55, 6)


def func2():
    return {'frkui': 34, 'mgukl': 84, 'oagtc': 78}


def func3():
    return 3


def func4():
    return 'amgud'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
