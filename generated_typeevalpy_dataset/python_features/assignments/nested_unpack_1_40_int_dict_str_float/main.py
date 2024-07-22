# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 34


def func2():
    return {'aubab': 51, 'wibut': 11, 'fdycx': 54}


def func3():
    return 'zyoxv'


def func4():
    return 58.49


(a, b), (c, d) = [(func1, func2), (func3, func4)]
