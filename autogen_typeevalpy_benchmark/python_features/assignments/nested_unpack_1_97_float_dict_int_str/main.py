# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 65.94


def func2():
    return {'tfvho': 61, 'hctgb': 13, 'xfgci': 88}


def func3():
    return 99


def func4():
    return 'dzzeq'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
