# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 49


def func2():
    return 30.57


def func3():
    return {'yefwl': 52, 'yfuux': 53, 'jwmel': 44}


def func4():
    return 'cheir'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
