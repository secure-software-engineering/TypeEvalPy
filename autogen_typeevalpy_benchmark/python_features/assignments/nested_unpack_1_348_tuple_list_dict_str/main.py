# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (60, 26, 34)


def func2():
    return [90, 22, 7]


def func3():
    return {'klgcj': 35, 'ydslx': 37, 'lrdse': 96}


def func4():
    return 'mdwpz'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
