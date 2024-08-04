# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (86, 2, 97)


def func2():
    return 10.55


def func3():
    return {'dppfr': 9, 'adthp': 13, 'jwupn': 75}


def func4():
    return 'tnsze'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
