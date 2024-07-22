# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 76


def func2():
    return {'wypus': 22, 'pufqq': 16, 'kviuo': 46}


def func3():
    return 'axkyc'


def func4():
    return (97, 6, 88)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
