# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'gwjnj'


def func2():
    return {'wvsxv': 10, 'rwzno': 91, 'opgui': 19}


def func3():
    return 79.59


def func4():
    return 2


(a, b), (c, d) = [(func1, func2), (func3, func4)]
