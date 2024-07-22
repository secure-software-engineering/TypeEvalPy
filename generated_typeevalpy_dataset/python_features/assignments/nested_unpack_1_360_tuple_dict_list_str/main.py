# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return (47, 81, 85)


def func2():
    return {'cnnza': 50, 'zwggn': 33, 'zoglm': 54}


def func3():
    return [78, 47, 24]


def func4():
    return 'ceakz'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
