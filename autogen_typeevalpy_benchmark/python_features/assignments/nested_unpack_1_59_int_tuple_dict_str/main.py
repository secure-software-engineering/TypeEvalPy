# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 74


def func2():
    return (52, 91, 82)


def func3():
    return {'kcaiu': 44, 'qvxcv': 29, 'gpnki': 43}


def func4():
    return 'ubqnf'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
