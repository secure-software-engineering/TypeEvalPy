# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'mlndy'


def func2():
    return 25.36


def func3():
    return 2


def func4():
    return {'agwqw': 97, 'xnqem': 51, 'bqjxd': 74}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
