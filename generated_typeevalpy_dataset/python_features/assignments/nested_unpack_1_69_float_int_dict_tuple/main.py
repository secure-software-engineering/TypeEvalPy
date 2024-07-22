# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 48.65


def func2():
    return 97


def func3():
    return {'mefxj': 49, 'upzqv': 70, 'nmmdb': 40}


def func4():
    return (86, 47, 14)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
