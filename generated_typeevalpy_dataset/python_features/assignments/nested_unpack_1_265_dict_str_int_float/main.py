# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'gxieg': 70, 'maiea': 91, 'strpr': 7}


def func2():
    return 'wrfav'


def func3():
    return 26


def func4():
    return 30.12


(a, b), (c, d) = [(func1, func2), (func3, func4)]
