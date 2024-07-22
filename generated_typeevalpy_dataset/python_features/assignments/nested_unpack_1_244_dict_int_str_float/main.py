# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'isriy': 88, 'hclnv': 49, 'yuvep': 50}


def func2():
    return 37


def func3():
    return 'pxxqn'


def func4():
    return 28.18


(a, b), (c, d) = [(func1, func2), (func3, func4)]
