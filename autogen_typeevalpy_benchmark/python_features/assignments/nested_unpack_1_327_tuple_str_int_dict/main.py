# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (29, 43, 31)


def func2():
    return 'bocce'


def func3():
    return 19


def func4():
    return {'cretl': 19, 'gayrp': 70, 'jbimw': 29}


(a, b), (c, d) = [(func1, func2), (func3, func4)]
