# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'pmdbq'


def func2():
    return (75, 80, 10)


def func3():
    return {'mfdrn': 24, 'kwdzi': 100, 'zxzdw': 11}


def func4():
    return 63


(a, b), (c, d) = [(func1, func2), (func3, func4)]
