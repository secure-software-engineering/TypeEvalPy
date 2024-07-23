# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (98, 15, 35)


def func2():
    return 'wafxi'


def func3():
    return [43, 45, 6]


def func4():
    return {'lzvox': 17, 'bhdbi': 100, 'iosnm': 76}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
