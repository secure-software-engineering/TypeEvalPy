# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'gzutu': 25, 'lfrjd': 73, 'xmlhs': 24}


def func2():
    return 70


def func3():
    return 'jthvx'


def func4():
    return [71, 21, 9]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
