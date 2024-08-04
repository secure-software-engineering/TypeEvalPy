# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return [88, 33, 19]


def func2():
    return 84.1


def func3():
    return {'rhtav': 86, 'cwtwt': 7, 'oguuh': 49}


def func4():
    return 'kyzio'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
