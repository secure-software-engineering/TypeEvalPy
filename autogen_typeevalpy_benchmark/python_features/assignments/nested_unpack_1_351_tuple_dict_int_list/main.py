# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (32, 22, 27)


def func2():
    return {'wfdxo': 71, 'vwqqx': 33, 'nuwgc': 93}


def func3():
    return 70


def func4():
    return [53, 19, 48]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
