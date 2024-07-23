# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'bmqdy': 55, 'olosr': 76, 'nluae': 29}


def func2():
    return 29.86


def func3():
    return [54, 91, 24]


def func4():
    return 'wwcnb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
