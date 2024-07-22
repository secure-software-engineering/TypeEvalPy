# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'yyxks': 30, 'drvbw': 6, 'wuhqa': 38}


def func2():
    return 'udgbl'


def func3():
    return (47, 97, 75)


def func4():
    return 7


(a, b), (c, d) = [(func1, func2), (func3, func4)]
