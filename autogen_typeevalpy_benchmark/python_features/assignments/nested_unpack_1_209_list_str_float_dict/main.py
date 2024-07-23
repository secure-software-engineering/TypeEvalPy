# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [18, 32, 49]


def func2():
    return 'ahqir'


def func3():
    return 25.04


def func4():
    return {'myobz': 63, 'flyvy': 54, 'bxiir': 26}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
