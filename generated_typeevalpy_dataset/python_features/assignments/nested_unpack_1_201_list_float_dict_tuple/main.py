# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [7, 65, 8]


def func2():
    return 76.88


def func3():
    return {'vwfcq': 76, 'cmlmv': 28, 'ntkit': 86}


def func4():
    return (58, 1, 63)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
