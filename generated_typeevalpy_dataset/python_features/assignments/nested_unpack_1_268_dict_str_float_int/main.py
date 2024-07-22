# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ujlkl': 3, 'hkwno': 9, 'nwtod': 71}


def func2():
    return 'ziaso'


def func3():
    return 5.57


def func4():
    return 55


(a, b), (c, d) = [(func1, func2), (func3, func4)]
