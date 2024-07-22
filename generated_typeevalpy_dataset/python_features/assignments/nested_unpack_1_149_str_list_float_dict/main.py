# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'xjvhq'


def func2():
    return [55, 79, 39]


def func3():
    return 40.01


def func4():
    return {'mivfu': 17, 'xrzfr': 13, 'focdj': 65}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
