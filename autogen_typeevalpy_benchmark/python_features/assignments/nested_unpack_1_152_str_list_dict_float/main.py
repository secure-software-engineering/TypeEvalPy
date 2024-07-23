# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'yjssm'


def func2():
    return [96, 6, 63]


def func3():
    return {'jwjqe': 30, 'gldgd': 11, 'rdmyj': 66}


def func4():
    return 15.8


(a, b), (c, d) = [(func1, func2), (func3, func4)]
