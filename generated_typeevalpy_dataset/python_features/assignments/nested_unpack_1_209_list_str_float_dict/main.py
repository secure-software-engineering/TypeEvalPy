# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [91, 2, 32]


def func2():
    return 'metul'


def func3():
    return 30.29


def func4():
    return {'frhnh': 75, 'bzrhb': 46, 'ifqtb': 16}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
