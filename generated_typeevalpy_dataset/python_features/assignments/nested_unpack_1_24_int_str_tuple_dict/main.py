# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 95


def func2():
    return 'wxanw'


def func3():
    return (4, 16, 90)


def func4():
    return {'yehod': 88, 'pmahn': 19, 'ouorf': 85}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
