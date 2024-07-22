# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [43, 69, 25]


def func2():
    return 17.12


def func3():
    return {'ylnhm': 4, 'efwvr': 87, 'imlrs': 15}


def func4():
    return 26


(a, b), (c, d) = [(func1, func2), (func3, func4)]
