# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 23


def func2():
    return (29, 44, 77)


def func3():
    return {'xnjlr': 47, 'wymck': 88, 'ygvay': 36}


def func4():
    return 'zfaco'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
